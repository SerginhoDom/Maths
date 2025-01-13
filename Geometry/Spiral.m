t = 0:pi/50:10*pi;
figure;
for i = 1:1:length(t)
    clf;
    hold on;
    plot3(sin(t),cos(t),t)
    plot3(sin(t(i)), cos(t(i)), t(i), 'O');
    view(35, 35);
    xlabel('sin(t)')
    ylabel('cos(t)')
    zlabel('t')
    pause(0.1);
end;