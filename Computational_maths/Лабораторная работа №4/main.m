syms f(x)
f(x) = 4*x - cos(x);

a = 0.1;
b = 0.6;

nodes = linspace(0.1, 0.6, 11);
I1 = 0;
for i = 1:length(nodes)-1
        I1 = I1 + NewtonKotes(nodes(i), nodes(i + 1));
end
I = ingrationF(linspace(0.1, 0.6, 11), I1);