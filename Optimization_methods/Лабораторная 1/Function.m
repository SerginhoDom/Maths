function [y] = Function(x, A, b)
y = dot(1/2*transpose(x)*A,x) + dot(b,x);
end

