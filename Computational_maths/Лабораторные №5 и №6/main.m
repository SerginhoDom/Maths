syms f(x)
f(x) = 4*x - cos(x);
d1f = diff(f(x), 1);
nodes = linspace(0.1, 0.6, 11);
h = 0.05;

m0 = vpa(subs(d1f, x, nodes(1)));
mn = vpa(subs(d1f, x, nodes(end)));
cubicSplain = createCubicSplainMatrix(f(x), nodes);

arrayA = [0 -cubicSplain(1, 3)/cubicSplain(1, 2)];
arrayB = [0 cubicSplain(1, 4)/cubicSplain(1, 2)];

[arrayA, arrayB] = doStraightStroke(arrayA, arrayB, cubicSplain);
arrayM = doReverseStroke(arrayA, arrayB, cubicSplain);

answer = differentiationViaSplain(f(x), [m0 arrayM mn], h, 0.37);
disp(subs(vpa(answer), x, 0.37));
disp(vpa(subs(d1f, x, 0.37)));
disp(vpa(arrayM(1)));