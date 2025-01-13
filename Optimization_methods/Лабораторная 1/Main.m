% Создание положительно определенной матрицы 
A = [[1.0000    0.5000    0.3333    0.2500    0.2000    0.1667]; [0.5000    1.0000    0.6667    0.5000    0.4000    0.3333];...
[0.3333    0.6667    1.0000    0.7500    0.6000    0.5000]; [0.2500    0.5000    0.7500    1.0000    0.8000    0.6667];...
[0.2000    0.4000    0.6000    0.8000    1.0000    0.8333]; [0.1667    0.3333    0.5000    0.6667    0.8333    1.0000]];
e = eig(A);
x = [0.5688; 0.4694; 0.0119; 0.3371; 0.1622; 0.7943];
b = [0.3112; 0.5285; 0.1656; 0.6020; 0.2630; 0.6541];
counter = 0;
fx = zeros(1, 1);
mas = zeros(1, 1);
y = Function(x, A, b);
xmas = cell(1, 0);

Xe = SearchForExtremum(A, b);
epsilon = norm(GradientFunction(x, A, b) - x);
disp (y);

while (epsilon >= 10^(-6))
    x = GradientFunction(x, A, b);
    counter = counter + 1;
    epsilon = norm(GradientFunction(x, A, b) - x);
    fx(end+1) = Function(x, A, b);
    mas(end+1) = counter;
    xmas{end+1}= x;
end





disp('Положительно определенная матрица:');
disp (A);
disp (b);
disp (x);
disp (Xe);
disp (e);

disp('Промежуточные значения функции');
disp(fx((counter - mod(counter,4)) / 4));
disp(fx((counter - mod(counter,2)) / 2));
disp(fx(fix(counter * 0.75)));
disp(fx(counter));

disp('Промежуточные значения');
disp(xmas{(counter - mod(counter,4)) / 4});
disp(xmas{(counter - mod(counter,2)) / 2});
disp(xmas{fix(counter * 0.75)});S
disp(xmas{counter});

disp('Разница координат');
disp(abs(x(1) - Xe(1)));
disp(abs(x(2) - Xe(2)));
disp(abs(x(3) - Xe(3)));
disp(abs(x(4) - Xe(4)));
disp(abs(x(5) - Xe(5)));
disp(abs(x(6) - Xe(6)));

disp('Разница значений функции');
disp(abs(Function(x, A, b) - Function(Xe, A, b)));
disp(Function(x, A, b));

plot(mas, fx);