x = -2*pi:pi/30:2*pi;
y = -2*pi:pi/30:2*pi;

[X, Y] = meshgrid(x, y);

Z = (sin(X .* X + Y .* Y)) ./ (X .* X + Y .* Y);

figure;
surfc(X, Y, Z);
colormap autumn;

figure;
imagesc(x, y, Z);
colormap hsv;

figure;
contourf(x, y, Z);
colormap spring;

