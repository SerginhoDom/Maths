function w = calculateWForReminder(x, nodes)
    w = 1;
    for i = 1:length(nodes)
        w = w*(x - nodes(i));
    end
end