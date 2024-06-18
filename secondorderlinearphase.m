clear

w = 8;
phi = 2;
t = 0:0.01:3;
x = w/2/sqrt(phi^2-1)*(exp((-phi+sqrt(phi^2-1))*w*t)-exp((-phi-sqrt(phi^2-1))*w*t));
y = -(w*(w*exp(-t*w*(phi - (phi^2 - 1)^(1/2)))*(phi - (phi^2 - 1)^(1/2)) - w*exp(-t*w*(phi + (phi^2 - 1)^(1/2)))*(phi + (phi^2 - 1)^(1/2))))/(2*(phi^2 - 1)^(1/2));
plot(x,y,'b');

hold on

w = 3;
phi = 5;
t = 0:0.01:5;
xminus = -(w/2/sqrt(phi^2-1)*(exp((-phi+sqrt(phi^2-1))*w*t)-exp((-phi-sqrt(phi^2-1))*w*t)));
yminus = (w*(w*exp(-t*w*(phi - (phi^2 - 1)^(1/2)))*(phi - (phi^2 - 1)^(1/2)) - w*exp(-t*w*(phi + (phi^2 - 1)^(1/2)))*(phi + (phi^2 - 1)^(1/2))))/(2*(phi^2 - 1)^(1/2));

plot(xminus,yminus,'r');

hold off

set(gca,'XAxisLocation','origin','YAxisLocation','origin')

title('过阻尼情况（稳定节点）');