function [x_solution] = SearchForExtremum(A, b)  
    x_solution = -1 * A^(-1) * b;
end