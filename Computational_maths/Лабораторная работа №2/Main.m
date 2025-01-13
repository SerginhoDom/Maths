syms f(x)
f(x) = 4*x - cos(x);

intorpolationNodes = linspace(0.1, 0.6, 11);
computedX = [0.12, 0.57, 0.37];

disp(abs(vpa(f(0.12)) - vpa(Newton1(0.12, 0.1, 0.05, 10))))
[minR, maxR] = calculationMinAndMaxReminder(f(x), 0.12, intorpolationNodes);
disp(vpa(minR))
disp(vpa(maxR))

disp('__________')
disp(abs(vpa(f(0.57)) - vpa(Newton2(0.57, 0.55, 0.05, 10))))
[minR, maxR] = calculationMinAndMaxReminder(f(x), 0.57, intorpolationNodes);
disp(vpa(minR))
disp(vpa(maxR))

disp('__________')
h = vpa(Stirling(f(x), 0.35, 0.05, 10));
answer = vpa(subs(h,x,0.37));
disp(abs(vpa(f(0.37)) - answer))
[minR, maxR] = calculationMinAndMaxReminder(f(x), 0.37, intorpolationNodes);
disp(vpa(minR))
disp(vpa(maxR))