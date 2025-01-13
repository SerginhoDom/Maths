syms f(x)
f(x) = 4*x - cos(x);

intorpolationNodes = linspace(0.1, 0.6, 11);

L = intorpolationLagrangFormula(intorpolationNodes(2), intorpolationNodes(2:6));
DL = diff(L);
DF = diff(f(x));
DL = vpa(subs(DL, x, intorpolationNodes(4)));
DF = vpa(subs(DF, x, intorpolationNodes(4)));
disp(abs(DL - DF))

[minR, maxR] = calculationMinAndMaxReminder(f(x), intorpolationNodes(2), intorpolationNodes(1:5));
disp(minR);
disp(maxR);