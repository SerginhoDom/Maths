% Задаем сетку
x = linspace(0, 1, 25);
vector = ones(25, 1);

A = vander(x);
y = A*vector;
disp(y);
coef = A^-1 * y;
disp(cond(A));
disp(norm(vector - coef));

disp(A);
disp('Искомые коэффициенты');
disp(coef');
