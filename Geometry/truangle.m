m = [5 4];
n = [-3 -7];
k = [4, -2];
t = [0 0];

c = [10 10];


figure;
hold on;

m = m - c;
n = n - c;
k = k- c;
t = t - c;
 
for i = 0:1:180
      clf;
  alph = i * pi / 180;
  Ralph = [[cos(alph) (-sin(alph))]; [sin(alph) cos(alph)]];
  xlim([-15 35]);
  ylim([-15 35]);
  
  
  m1 = Ralph*(m');
  n1 = Ralph*(n');
  k1 = Ralph*(k');
  t1 = Ralph*(t');
   
  hold on;
   m1 = m1' + c;
   n1 = n1' + c;
   k1 = k1' + c;
   t1 = t1' + c;
   pause(0.01);
   plot([m1(1) n1(1)], [m1(2) n1(2)]);
   plot([k1(1) n1(1)], [k1(2) n1(2)]);
   plot([m1(1) k1(1)], [m1(2) k1(2)]);
   plot([m1(1) t1(1)], [m1(2) t1(2)]);
   plot([k1(1) t1(1)], [k1(2) t1(2)]);
   plot([n1(1) t1(1)], [n1(2) t1(2)]);
   
   pause(0.01);


   
    
end;
