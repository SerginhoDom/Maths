function In = ingrationF(nodes, I)
    [leftNodes, rightNodes] = devidSegment(nodes);
    leftIn = countIn(leftNodes);
    rightIn = countIn(rightNodes);

    if (abs(I - (leftIn + rightIn)) < 0.01) 
        In = leftIn + rightIn;
        return;
    else 
        In = ingrationF(leftNodes, leftIn) + ingrationF(rightNodes, rightIn);
    end 
end

