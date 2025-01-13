function [Norm] = NormCounter(Matrix, MatrixSize)
    %Формула для 6 варианта
    Norm = 1/MatrixSize * sqrt(sum(sum(abs(Matrix.^2))));
end

