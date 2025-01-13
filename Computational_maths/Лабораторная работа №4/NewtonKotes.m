function I = NewtonKotes(a, b)
    syms f(x)
    f(x) = 4*x - cos(x);

    sum = 0;
    for i = 1:2
        v = a + (i)*0.05/i;
        sum = sum + (vpa(subs(f(x), x, v)))/2;
    end

    I = (b-a) * sum;
end

