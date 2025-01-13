function answer = countFiniteDifferences(m, h, x0)
    syms f(x)
    f(x) = 4*x - cos(x);

    answer = 0;
    for i = 0:m
        answer = answer + ((-1)^(m-i))...
        *nchoosek(m, i)...
        *f(x0 + i*h);
    end
end

