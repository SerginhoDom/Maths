function answer = countXForChorda(func, lastX, lastTangentX)
    syms f(x) 
    f(x) = func;

    answer = lastX - (vpa(subs(f(x), x, lastX))*(lastTangentX - lastX))/...
        vpa((subs(f(x), x, lastTangentX)-subs(f(x), x, lastX)));
end

