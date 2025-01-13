function [A, B] = doStraightStroke(arrayA, arrayB, cubicSplain)
    for i=3:length(cubicSplain)
        arrayA(i) = -cubicSplain(i-1, 3)/... 
            (cubicSplain(i-1, 1)*arrayA(i-1) + cubicSplain(i-1, 2));

        arrayB(i) = (cubicSplain(i-1, 4) - cubicSplain(i-1, 1)*arrayB(i-1))/...
            (cubicSplain(i-1, 1)*arrayA(i-1) + cubicSplain(i-1, 2));
    end
    A = arrayA;
    B = arrayB;
end

