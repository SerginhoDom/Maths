x = dlmread('data3.csv');
time = x(1:end, 1);
gx = x (1:end, 2);
gy = x(1:end, 3);
gz = x (1:end, 4);
gt = atan(sqrt(gx.^2 + gy.^2)) * 180 / pi;
z = gx + gy*1i;
psi = unwrap(angle(z));
psi = psi./pi * 180;
%unwrap(psi);

figure;
hold on;
plot(time, gx, 'color', 'r');
plot(time, gy, 'color', 'g');
plot(time, gz, 'color', 'b');
figure
hold on;
plot(time, gt, 'color', 'black');
figure;
hold on;
plot(time, psi, 'color', 'r');
