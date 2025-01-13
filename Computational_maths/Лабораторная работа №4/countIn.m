function In = countIn(nodes)
    In = 0;
    for i = 1:length(nodes)-1
        In = In + NewtonKotes(nodes(i), nodes(i + 1));
    end
end

