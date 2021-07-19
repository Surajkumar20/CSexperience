%% Messing with ODE45
t0 = 0;      %initial time
T = 1.5;     %seconds after starting
y0 = [0;0];  %Initial conditions

fhandle = functionHandleboi(3.255e7, 3.3e8, 2.085e12, 5.68e10, 126.55);

[ts,ys] = ode45(fhandle, [t0, T], y0);
plot(ts,ys(:,1),'b')              % plot solution y(t)
title('Solution y(t) of IVP')
xlabel('t'); grid on
ylim([-0.4, 0.4]);

%% A function that can return a function handle, as required for 0DE45's call
function output = functionHandleboi(m, c, k, F0, wn)
    output = @(t,x) [x(2); (F0*cos(wn*t)-c*x(2)-k*x(1))/m];
end
