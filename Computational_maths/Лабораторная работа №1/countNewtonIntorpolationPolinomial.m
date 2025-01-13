function answer = countNewtonIntorpolationPolinomial(computedX, indexMiddleNode, nodes, func)
    term1 = calculateIntorpolatedFunction(computedX);

    term2 = calculationNewtonDividedDifference(func, nodes(indexMiddleNode:indexMiddleNode + 1));
    term2 = term2*(computedX - nodes(indexMiddleNode));

    answer = term1 + term2;
end 