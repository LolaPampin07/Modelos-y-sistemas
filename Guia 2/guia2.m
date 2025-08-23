clc
clear  
%%%%%%%%%%%%%%%%%%%%%%%%EJERCICIO 2%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tspan = [0 12];
y0 = 30000;
f= @(t,y) 0.2 * y;
[t, y] =  ode45(f, tspan, y0);
y_10 = interp1(t, y, 10);
fprintf('A las 10 horas hay %f bacterias', y_10)
figure(1)
plot(t, y)
grid("on")
%%%%%%%%%%%%%%%%%%%%%%%%EJERCICIO 5%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tspan = [0 20];
g= @(t, y) -y+t;
y0_vals = -10:1:10;
for y0 = y0_vals
    [t, y] = ode23(g, tspan, y0);
    figure(2)
    hold on
    grid on
    plot(t,y)
end

%%%%%%%%%%%%%%%%%%%%%%%%EJERCICIO 8%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%parametros del sistema
m=5;
c=1000;
k=750;

%funcion del sistema
f=@(t,x) [x(2);-(c/m)*x(2)-(k/m)*x(1)]; %hago una matriz

%condiciones iniciales
x0=[1;0.5]; %el ; genera columnas

%intervalo de integracion
tspan= [0 10];

%resolver con ode45
[t,x]=ode45(f,tspan,x0);