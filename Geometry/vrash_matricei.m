
a = [0; 0; -1; 7];
b = [1; 2; 2; 2];
c = [0;-1; 2;3];
x1 = a;
y1 = b;
z1 = c;
figure
grid on

for ii = 1:60
    clf
    hold on
    q = ii/180*pi;
    n = [1 2 -1];
    len  = sqrt(n(1)^2 + n(2)^2 + n(3)^2);
    x = n(1)/len;
    y = n(2)/len;
    z = n(3)/len;
    rotor = [cos(q)+(1-cos(q))*(x^2) (1-cos(q))*x*y-(sin(q))*z (1-cos(q))*x*z+(sin(q))*y;
    (1-cos(q))*y*x+(sin(q))*z cos(q)+(1-cos(q))*(y^2) (1-cos(q))*y*z - sin(q)*x;
    (1-cos(q))*z*x-(sin(q))*y (1-cos(q))*z*y+(sin(q))*x cos(q)+(1-cos(q))*(z^2)];
    for jj = 1:4
        m = [a(jj) b(jj) c(jj)];
        m = m * rotor;
        x1(jj) = m(1);
        y1(jj) = m(2);
        z1(jj) = m(3);
    end

    view(30,30);
    plot3([x1(1) x1(2)], [y1(1) y1(2)], [z1(1) z1(2)]);
    plot3([x1(1) x1(3)], [y1(1) y1(3)], [z1(1) z1(3)]);
    plot3([x1(1) x1(4)], [y1(1) y1(4)], [z1(1) z1(4)]);
    plot3([x1(3) x1(4)], [y1(3) y1(4)], [z1(3) z1(4)]);
    plot3([x1(2) x1(3)], [y1(2) y1(3)], [z1(2) z1(3)]);
    plot3([x1(2) x1(4)], [y1(2) y1(4)], [z1(2) z1(4)]);
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    axis([-15 15 -15 15 -15 15]);
    grid on
    drawnow
end