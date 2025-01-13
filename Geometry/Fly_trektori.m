X = [];
Y = [];
Z = [];

from = [43.1207, 131,9045];
to = [55.7579, 37.6183];

delta_b = (from(2) - to(2)) * pi / 180;
k1 = tan(from(1) * pi / 180) / tan(delta_b);
k2 = tan(to(1) * pi / 180) / sin(delta_b);
 
R = 6371;

for b = 0:0.1:95
    b_radian = b * pi / 180;
    tg_alph = (k2 - k1) * sin(b_radian) - k1 * cos(b_radian);
    alph_radian = atan(tg_alph);
    
    x = R  * cos(alph_radian) * cos(b_radian);
    y = R * cos(alph_radian) * sin(b_radian);
    z = R * sin(alph_radian);
    
    X = [X x];
    Y = [Y -y];
    Z = [Z z];
end
figure;
for i = 1:1:length(X)
    clf;
    hold on;
    
    plot3(X, Y, Z, 'color', 'white', 'linewidth', 2);
    view(58, 13);
    [x, y, z] = sphere;
    surfc(x * R, y * R, z * R);
    plot3(X(i), Y(i), Z(i), 'o', 'linewidth', 4);
    pause(0.1);
end;
