x =-5:0.1:5;
y =-5:0.1:5;
[X, Y] = meshgrid(x, y);
z = sin(X.^2 + Y.^2)./(X.^2 + Y.^2);
hold on;
imagesc(x, y, z)
figure;
surfc(X, Y, z)
colormap autumn;
figure;
contour(z)