A = [0 1 0,1];
B = [0 2 -1,1];
C = [-1 2 2,1];
D = [7 2 3,1];

planeA = [1 -2 -1,4];

AB = [A(1,[1,2,3]);B(1,[1,2,3])]';
BC = [B(1,[1,2,3]);C(1,[1,2,3])]';
CA = [C(1,[1,2,3]);A(1,[1,2,3])]';
AD = [A(1,[1,2,3]);D(1,[1,2,3])]';
BD = [B(1,[1,2,3]);D(1,[1,2,3])]';
CD = [C(1,[1,2,3]);D(1,[1,2,3])]';

A0 = calculate(planeA,A);
B0 = calculate(planeA,B);
C0 = calculate(planeA,C);
D0 = calculate(planeA,D);

AB0 = [A0(1,[1,2,3]);B0(1,[1,2,3])]';
BC0 = [B0(1,[1,2,3]);C0(1,[1,2,3])]';
CA0 = [C0(1,[1,2,3]);A0(1,[1,2,3])]';
AD0 = [A0(1,[1,2,3]);D0(1,[1,2,3])]';
BD0 = [B0(1,[1,2,3]);D0(1,[1,2,3])]';
CD0 = [C0(1,[1,2,3]);D0(1,[1,2,3])]';

hold on

xlim([-7 7]);
ylim([-7 7]);
zlim([-7 7]);
%------------------------------------------------------------
X = AB(1,[1,2]);
Y = AB(2,[1,2]);
Z = AB(3,[1,2]);
line(X,Y,Z);

X = BC(1,[1,2]);
Y = BC(2,[1,2]);
Z = BC(3,[1,2]);
line(X,Y,Z);

X = CA(1,[1,2]);
Y = CA(2,[1,2]);
Z = CA(3,[1,2]);
line(X,Y,Z);

X = AD(1,[1,2]);
Y = AD(2,[1,2]);
Z = AD(3,[1,2]);
line(X,Y,Z);

X = BD(1,[1,2]);
Y = BD(2,[1,2]);
Z = BD(3,[1,2]);
line(X,Y,Z);

X = CD(1,[1,2]);
Y = CD(2,[1,2]);
Z = CD(3,[1,2]);
line(X,Y,Z);
%------------------------------------------------------------
X = AB0(1,[1,2]);
Y = AB0(2,[1,2]);
Z = AB0(3,[1,2]);
line(X,Y,Z);

X = BC0(1,[1,2]);
Y = BC0(2,[1,2]);
Z = BC0(3,[1,2]);
line(X,Y,Z);

X = CA0(1,[1,2]);
Y = CA0(2,[1,2]);
Z = CA0(3,[1,2]);
line(X,Y,Z);

X = AD0(1,[1,2]);
Y = AD0(2,[1,2]);
Z = AD0(3,[1,2]);
line(X,Y,Z);

X = BD0(1,[1,2]);
Y = BD0(2,[1,2]);
Z = BD0(3,[1,2]);
line(X,Y,Z);

X = CD0(1,[1,2]);
Y = CD0(2,[1,2]);
Z = CD0(3,[1,2]);
line(X,Y,Z);
%------------------------------------------------------------

A = [0 1 0,1]
B = [0 2 -1,1]
C = [-1 2 2,1]

planeB = [1,-2,-1,4]

Ap = calculate(planeB,A)
Bp = calculate(planeB,B)
Cp = calculate(planeB,C)

function [t] = t_param(planeA,dotM)
    t = dot(planeA,dotM);
    t = (-1)*(t/(planeA(1)^2+planeA(2)^2+planeA(3)^2));
end

function [dot0] = calculate(planeA,dotM)
    t = t_param(planeA,dotM);
    dot0(1) = planeA(1)*t+dotM(1);
    dot0(2) = planeA(2)*t+dotM(2);
    dot0(3) = planeA(3)*t+dotM(3);
end

