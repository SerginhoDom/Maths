function answer = countNewtonIntorpolationPolinomial2(computedX, indexMiddleNode, nodes, func)
    term1 = calculateIntorpolatedFunction(nodes(indexMiddleNode - 1));

    term2 = calculationNewtonDividedDifference(func, nodes(indexMiddleNode - 1:indexMiddleNode));
    term2 = term2*(computedX - nodes(indexMiddleNode - 1));

    term3 = calculationNewtonDividedDifference(func, nodes(indexMiddleNode - 1: indexMiddleNode + 1));
    term3 = term3*(computedX - nodes(indexMiddleNode - 1))*(computedX - nodes(indexMiddleNode));

    answer = term1 + term2 + term3;
end 