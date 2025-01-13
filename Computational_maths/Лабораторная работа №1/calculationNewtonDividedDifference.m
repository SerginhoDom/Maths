function dividedDiffrence = calculationNewtonDividedDifference(func, nodes)
    syms f(x)
    f(x) = func;
    if length(nodes) == 2
        dividedDiffrence = (vpa(f(nodes(2))) - vpa(f(nodes(1))))/(nodes(2) - nodes(1));
        return;
    else 
    dividedDiffrence = calculationNewtonDividedDifference(f(x), nodes(2:end)) - calculationNewtonDividedDifference(f(x), nodes(1:end-1));
    dividedDiffrence = dividedDiffrence / (nodes(end) - nodes(1));
    end
end 
