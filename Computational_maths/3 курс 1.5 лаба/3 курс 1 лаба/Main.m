disp(['k', '    ', 'Норма матрицы ||A|| ', '   ', 'cond(A) ']);

for k = 1:5
    % Генерация матрицы 25x25 со случайными числами от 0 до 1
    MatrixSize = 25;
    A = MatrixGenerator(MatrixSize);
    
    % Вычисление нормы с помощью функции
    norm_A = NormCounter(A, MatrixSize);
    
    % Вычисление числа обусловленности
    cond_A = cond(A);

    
    % Вывод результатов
    disp([num2str(k), '    ', num2str(norm_A), '                 ', num2str(cond_A)]);
end