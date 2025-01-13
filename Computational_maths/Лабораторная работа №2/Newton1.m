function answer = Newton1(xx, x0, h, n)
    syms f(x)
    f(x) = 4*x - cos(x);

    t = (xx - x0)/h;
    answer = vpa(f(x0));
    for i = 1:n
        fv = countFiniteDifferences(i, h, x0);
        fact = factorial(i);
        compositionT = 1;
        for j = 1:i
            compositionT = compositionT * (t - j+1);
        end
        answer = answer + fv*compositionT/fact;
    end
end