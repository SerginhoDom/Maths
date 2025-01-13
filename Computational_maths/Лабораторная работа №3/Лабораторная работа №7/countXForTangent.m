function answer = countXForTangent(func, lastX)
    syms f(x) 
    f(x) = func;
    D1f = diff(f(x), 1);

    answer = lastX -(vpa(subs(f(x), x, lastX)/subs(D1f, x, lastX)));
end

