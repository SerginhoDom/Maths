function indexNearestNode = findIndexNearestNode(x, nodes)
    indexNearestNode = 1;
    maxNode = max(nodes);
    for i = 1:length(nodes)
        nodes(i) = abs(nodes(i) - x);
        if nodes(i) < maxNode
            maxNode = nodes(i);
            indexNearestNode = i;
        end
    end
end