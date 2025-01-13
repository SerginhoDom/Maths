syms f(x) 
f(x) = x*log10(x) - 1/2;
Df = diff(f(x), 1);
D2f = diff(f(x), 2);

a = vpa(subs(Df, x, 1));
b = vpa(subs(Df, x, 5));
a2 = vpa(subs(D2f, x, 2));
b2 = vpa(subs(D2f, x, 5));

tangents = [1];
hords = [5];

answer = findZeroX(f(x), tangents, hords);