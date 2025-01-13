%% Исследуемая функция 
syms f(x)
f(x) = 4*x - cos(x);
%% Входные данные 
intorpolationNodes = linspace(0.1, 0.6, 11);
computedX = 0.37;

%% Находим ближайшее значение функции к точке
indexNearestNode = findIndexNearestNode(computedX, intorpolationNodes);
functionValueInComputedX = vpa(f(computedX));
fprintf('f(%s) = %s for x = %f\n\n', f(x), functionValueInComputedX, computedX); 

%% Лагранж первого порядка
L1 = intorpolationLagrangFormula(0.37, intorpolationNodes(indexNearestNode:indexNearestNode + 1));
R1 = L1 - functionValueInComputedX;
[minR, maxR] = calculationMinAndMaxReminder(f(x), computedX, intorpolationNodes(indexNearestNode:indexNearestNode + 1));

fprintf('Lagrange1 = %s\n', vpa(L1));
estimateErrorString = sprintf('%f < %s < %f\n', minR, R1, maxR);
disp(estimateErrorString);
%% Лагранж второго порядка
L2 = intorpolationLagrangFormula(0.37, intorpolationNodes(indexNearestNode - 1 : indexNearestNode + 1));
R2 = L2 - functionValueInComputedX;
[minR2, maxR2] = calculationMinAndMaxReminder(f(x), computedX, intorpolationNodes(indexNearestNode-1:indexNearestNode + 1));

fprintf('Lagrange2 = %s\n', vpa(L2));
estimateErrorString2 = sprintf('%f < %s < %f\n', minR2, abs(R2), maxR2);
disp(estimateErrorString2);

%% Полином Ньютона первого порядка
newtonPolinom1 = countNewtonIntorpolationPolinomial(0.37, indexNearestNode, intorpolationNodes,  f(x));
fprintf('newtonPolinom1 = %s\n', newtonPolinom1);

%% Полином Ньютона второго порядка
newtonPolinom2 = countNewtonIntorpolationPolinomial2(0.37, indexNearestNode, intorpolationNodes, f(x));
fprintf('newtonPolinom2 = %s\n', newtonPolinom2);