function answer = differentiationViaSplain(func, arrayM, h, x)
    syms f(x)
    xi = 0.35;
    f(x) = func;
        answer = (subs(f(x), x, (xi + h)) - subs(f(x), x, xi))/h ...
        - h/6*(2*arrayM(5) + arrayM(6)) ...
        + arrayM(5)*(x - xi) + (arrayM(6) - arrayM(5))/(2*h)*(x - xi)^2;
    
end

