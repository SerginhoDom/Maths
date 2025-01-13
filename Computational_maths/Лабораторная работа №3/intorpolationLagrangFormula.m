function answer = intorpolationLagrangFormula(x, nodes)
    answer = 0;
    for i = 1:length(nodes)
        answer = answer + calculateIntorpolatedFunction(nodes(i))*countBasicPolynomials(nodes, i);
    end
end