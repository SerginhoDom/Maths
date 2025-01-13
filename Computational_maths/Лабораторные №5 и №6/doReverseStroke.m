function answer = doReverseStroke(arrayA, arrayB, cubicSplain)
    xn = (cubicSplain(end, 4) - cubicSplain(end, 1)*arrayB(end))/...
        (cubicSplain(end, 2) + cubicSplain(end, 1)*arrayA(end));

    arrayX = [];
    arrayX(length(arrayA)) = xn;

    for i=length(arrayA)-1:-1:1
        arrayX(i) = arrayA(i+1)*arrayX(i+1) + arrayB(i + 1);
    end
    
    answer = arrayX;
end

