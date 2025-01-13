function [leftNodes, rightNodes] = devidSegment(oldNodes)
    center = (oldNodes(end) - oldNodes(1))/2;
    leftNodes = linspace(oldNodes(1), center, 11);
    rightNodes = linspace(center, oldNodes(end), 11);
end

