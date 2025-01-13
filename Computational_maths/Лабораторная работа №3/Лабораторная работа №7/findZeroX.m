function answer = findZeroX(func, tangets, hords)
    syms f(x)
    f(x) = func;
    tangets(end + 1) = countXForTangent(f(x), tangets(end));
    hords(end + 1) = countXForChorda(f(x), hords(end), tangets(end-1));

    if (abs(tangets(end) - hords(end)) < 0.001)
        answer = hords(end);
        return;
    else 
        answer = findZeroX(f(x), tangets, hords);
    end
end

