function [out] = Finitdiffcentral(f,x0,h,N)
    syms x;
    out = 0;
    if(mod(N,2) == 0)   
        for i = 0:N
            out = out + (-1)^(i)*nchoosek(N,i)*subs(f,x,x0+((N/2)-i)*h);
        end
    else
        for i = 0:N
            out = out + (-1)^(i)*nchoosek(N,i)*subs(f,x,x0+((N/2)-i)*h - h/2);
        end
        for i = 0:N
            out = out + (-1)^(i)*nchoosek(N,i)*subs(f,x,x0+((N/2)-i)*h + h/2);
        end
        out = out / 2;
    end
    
end

