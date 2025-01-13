function answer = countRightColumn(func, nodes, i)
    syms f(x)
    f(x) = func;

    h = nodes(i + 1)  - nodes(i);
    answer = (6/(2*h))*...
        ( ...
        (subs(f(x), x, nodes(i + 1)) - subs(f(x), x, nodes(i)))/h -...
        (subs(f(x), x, nodes(i)) - subs(f(x), x, nodes(i - 1)))/h...
        );

    answer = vpa(answer);
end

