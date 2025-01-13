cos_alph = zeros(1, 100);

for n = 1:1:100
    cos_alph(1, n) = (n-1)/(sqrt(n-1) * sqrt(n));
end;
figure;
plot(cos_alph);