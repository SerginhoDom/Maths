function answer = countBasicPolynomials(nodes, i)
    syms x
    answer = 1;
    for j = 1:length(nodes)
        if j == i
            continue;
        end
        answer = answer*(x - nodes(j))/(nodes(i) - nodes(j));
    end
end 