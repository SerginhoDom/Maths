function [Xn] = GradientFunction(x, A, b)
%Xn - Next X
Xn = x;
Learning_rate = 10^(-4);
Xn = x - Learning_rate * DerivativeFunction(x, A, b);
end