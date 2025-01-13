m = [5 8];
k = [1 1];
z = [10 10];


x = [-10:0.1:10];
y = -x/sqrt(3) - 4/sqrt(3);

alph = atan(-1/sqrt(3));
Ralph = [[cos(alph) (-sin(alph))]; [sin(alph) cos(alph)]];
Ralph1 = [[cos(alph) (sin(alph))]; [-sin(alph) cos(alph)]];

figure;
hold on;
xlim([-20 20]);
ylim([-20 20]);

plot([m(1) k(1)], [m(2) k(2)]);
plot([m(1) z(1)], [m(2) z(2)]);
plot([z(1) k(1)], [z(2) k(2)]);

plot(x, y, 'color', 'green');

x1 = cos(alph)*x +sin(alph)*y;
y1 = -sin(alph)*x + cos(alph)*y;

m1 = Ralph1*(m');
z1 = Ralph1*(z');
k1 = Ralph1*(k');


m1(2) = 2 * y1(1) - m1(2);
z1(2) = 2 * y1(1) - z1(2);
k1(2) = 2 * y1(1) - k1(2);



m1 = Ralph*(m1);
z1 = Ralph*(z1);
k1 = Ralph*(k1);

plot([m1(1) k1(1)], [m1(2) k1(2)], 'color', 'r');
plot([m1(1) z1(1)], [m1(2) z1(2)], 'color', 'r');
plot([z1(1) k1(1)], [z1(2) k1(2)], 'color', 'r');

