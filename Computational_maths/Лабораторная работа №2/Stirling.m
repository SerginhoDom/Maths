function [out] = Stirling(f,x0,h,N)
    syms x;
    out = subs(f,x,x0);
    t = (x - x0)/h;
    for i = 1:2*N
        
        summand = Finitdiffcentral(f,x0,h,i);
        summand = summand * t ^ (2-mod(i,2));
        
        for j = 2:round(i/2)
            summand = summand * (t^(2)-(j-1)^2);
        end
        
        out = out + summand / factorial(i);
    end
end

