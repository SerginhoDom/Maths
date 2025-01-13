function [y] = DerivativeFunction(x, A, b)
y = 1/2 * (transpose(A) + A)*x + b;
end

