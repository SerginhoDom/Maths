r = 10;%Радиус
a = 10;%Центр абсциссы
b = 10;%Центральная ордината
theta = 0:pi/180:2*pi; %угол[0,2*pi] 
x = a+r*cos(theta);
y = b+r*sin(theta);
plot(x,y,'-')
axis equal