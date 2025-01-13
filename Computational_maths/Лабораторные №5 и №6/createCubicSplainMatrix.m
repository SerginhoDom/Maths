function answer = createCubicSplainMatrix(func, nodes)
    m = [];
    for i=2:length(nodes)-1
        m(i-1, 1) = 1/2;
        m(i-1, 2) = 2;
        m(i-1, 3) = 1/2;
        m(i-1, 4) = countRightColumn(func, nodes, i);
    end
    answer = m;
end

