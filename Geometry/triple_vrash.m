close all;
figure;
X = [1 5 -3 9]';
Y = [8 7 3 1]';
Z = [6 9 5 2]';
X1 = [1 5 -3 9]';
Y1 = [8 7 3 1]';
Z1 = [6 9 5 2]';
T = [1 2 3; 1 2 4; 2 3 4; 1 3 4];
hold on;
trisurf(T,X,Y,Z);
tett = 1:1:180;

for ii = 1:length(tett)
    clf;
    hold on;
    xlim([-15 15]);
    ylim([-15 15]);
    zlim([-15 15]);
    view(28, 31);
    plot3([0 0], [0 0], [-15 15], 'color', 'b');
    plot3([0 0], [-15 15], [0 0], 'color', 'g');
    plot3([-15 15], [0 0], [0 0], 'color', 'r');
    tetta = tett(ii) / 180 * pi;
    vector = [4 3 2];
    del = sqrt(vector(1)^2 + vector(2)^2 +vector(3)^2);
    q = [cos(tetta) sin(tetta)*vector(1)/del sin(tetta)*vector(2)/del sin(tetta)*vector(3)/del];
    qt = [cos(tetta) -sin(tetta)*vector(1)/del -sin(tetta)*vector(2)/del -sin(tetta)*vector(3)/del];
    for i = 1:4
        vector = [0 X(i) Y(i) Z(i)];
        vector = multiple(multiple(q, vector), qt);
        X1(i) = vector(2); Y1(i) = vector(3); Z1(i) = vector(4);
    end;
    trisurf(T,X1,Y1,Z1);
    
    pause(0.00003);
end