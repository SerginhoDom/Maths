

A = [0 1 0];
B = [0 2 -1];
C = [-1 2 2];
D = [7 2 3];
a = [1 -2 -1];
Ta = t_find(A,a);
Tb = t_find(B,a);
Tc = t_find(C,a);
Td = t_find(D,a);
At = projection(A,Ta,a);
Bt = projection(B,Tb,a);
Ct = projection(C,Tc,a);
Dt = projection(D,Td,a);

ort_1 = Ct-At;
ort_2 = cross(a,ort_1);
ort_1 = ort_1./(sqrt(ort_1(1).^2+ort_1(2).^2+ort_1(3).^2));
ort_2 = ort_2./(sqrt(ort_2(1).^2+ort_2(2).^2+ort_2(3).^2));

Ax_y = X_Y(At,ort_1,ort_2);
Bx_y = X_Y(Bt,ort_1,ort_2);
Cx_y = X_Y(Ct,ort_1,ort_2);
Dx_y = X_Y(Dt,ort_1,ort_2);

hold on


axis("auto");
plot3([At(1) Bt(1)],[At(2) Bt(2)],[At(3) Bt(3)]);
plot3([At(1) Ct(1)],[At(2) Ct(2)],[At(3) Ct(3)]);
plot3([At(1) Dt(1)],[At(2) Dt(2)],[At(3) Dt(3)]);
plot3([Bt(1) Ct(1)],[Bt(2) Ct(2)],[Bt(3) Ct(3)]);
plot3([Bt(1) Dt(1)],[Bt(2) Dt(2)],[Bt(3) Dt(3)]);
plot3([Dt(1) Ct(1)],[Dt(2) Ct(2)],[Dt(3) Ct(3)]);

plot3([A(1) B(1)],[A(2) B(2)],[A(3) B(3)]);
plot3([A(1) C(1)],[A(2) C(2)],[A(3) C(3)]);
plot3([A(1) D(1)],[A(2) D(2)],[A(3) D(3)]);
plot3([B(1) C(1)],[B(2) C(2)],[B(3) C(3)]);
plot3([B(1) D(1)],[B(2) D(2)],[B(3) D(3)]);
plot3([D(1) C(1)],[D(2) C(2)],[D(3) C(3)]);
drawnow
figure
hold on
plot([Ax_y(1) Bx_y(1)],[Ax_y(2) Bx_y(2)]);
plot([Ax_y(1) Cx_y(1)],[Ax_y(2) Cx_y(2)]);
plot([Ax_y(1) Dx_y(1)],[Ax_y(2) Dx_y(2)]);
plot([Bx_y(1) Cx_y(1)],[Bx_y(2) Cx_y(2)]);
plot([Bx_y(1) Dx_y(1)],[Bx_y(2) Dx_y(2)]);
plot([Dx_y(1) Cx_y(1)],[Dx_y(2) Cx_y(2)]);
drawnow


function[t] = t_find(A,a)
t = -1.*(a(1).*A(1)+a(2).*A(2)+a(3).*A(3))/(a(1).^2+a(2).^2+a(3).^2);
end

function[At] = projection(A,t,a)
At(1) = a(1).*t+A(1);
At(2) = a(2).*t+A(2);
At(3) = a(3).*t+A(3);
end

function[A] = X_Y(At,ort_1,ort_2)
A(1) = At*ort_1';
A(2) = At*ort_2';
end