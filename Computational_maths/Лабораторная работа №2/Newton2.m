function answer = Newton2(xx, xn, h, n)
    syms f(x)
    f(x) = 4*x - cos(x);
    
    t = (xx - xn)/h;
    answer = vpa(f(xn));
    for i = 1:n
        fv = countFiniteDifferences(i, h, xn-h*i);
        fact = factorial(i);
        compositionT = 1;
        for j = 1:i
            compositionT = compositionT * (t + j - 1 );
        end
        answer = vpa(answer + fv*compositionT/fact);
    end
end 