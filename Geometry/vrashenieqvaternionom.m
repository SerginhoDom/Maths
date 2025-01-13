close all;
figure;


X = [5 -1 -7 4]';
Y = [9 5 2 14]';
Z = [5 1 5 2]';
X1 = X;
Y1 = Y;
Z1 = Z;
T = [1 2 3; 1 2 4; 2 3 4; 1 3 4];
hold on;


trisurf(T,X,Y,Z);
tett = 1:1:180;

for i1 = 1:length(tett)
    clf;
    hold on;

    xlim([-20 20]);
    ylim([-20 20]);
    zlim([-20 20]);
    view(28, 31);
    plot3([0 0], [0 0], [-20 20], 'color', 'r');
    plot3([0 0], [-20 20], [0 0], 'color', 'g');
    plot3([-20 20], [0 0], [0 0], 'color', 'b');

    tetta = tett(i1) / 180 * pi;
    vector = [0 0 1];

    del = sqrt(vector(1) + vector(2) +vector(3));
    q1 = [cos(tetta) sin(tetta)*vector(1)/del sin(tetta)*vector(2)/del sin(tetta)*vector(3)/del];
    q2 = [cos(tetta) -sin(tetta)*vector(1)/del -sin(tetta)*vector(2)/del -sin(tetta)*vector(3)/del];

    for i = 1:4
        vector = [0 X(i) Y(i) Z(i)];
        vector = multiple(multiple(q1, vector), q2);
        X1(i) = vector(2); Y1(i) = vector(3); Z1(i) = vector(4);
    end;
    trisurf(T,X1,Y1,Z1);
    pause(0.005);
end

function [ z ] = multiple( z1, z2 )
z(1) = (z1(1) * z2(1)) - (z1(2) * z2(2) + z1(3) * z2(3) + z1(4) * z2(4));
z(2) = (z1(1) * z2(2)) + (z2(1) * z1(2)) + (z1(3)*z2(4) - z1(4)*z2(3));
z(3) = (z1(1) * z2(3)) + (z2(1) * z1(3)) + (z1(4)*z2(2) - z1(2)*z2(4));
z(4) = (z1(1) * z2(4)) + (z2(1) * z1(4)) + (z1(2)*z2(3) - z1(3)*z2(2));
end