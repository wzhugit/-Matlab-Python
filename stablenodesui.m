clear

fig = uifigure("Name","2个负实数根----对应稳定节点，为过阻尼情形","Units","normalized","Position",[0.3,0.3,0.5,0.5]);

ax = uiaxes("Parent",fig,"Units","normalized","Position",[0.1,0.2,0.7,0.6]);

slides = uislider(fig,"Position",[70,65,80,3],"Limits",[1,2],"Value",1,"ValueChangingFcn",@(slides,event)ValueChanging(slides,ax));

uilabel(fig,"Position",[50,20,100,50],"Interpreter","latex","Text","$$\xi$$");

uilabel(fig,"Position",[100,450,500,40],"Interpreter","latex","Text",'不同阻尼比\xi下二阶过阻尼系统的相平面图','FontName','KaiTi','FontSize',20);

function ValueChanging(slides,ax)

phi = slides.Value;

w = 8;

t = 0:0.02:3;
x = w/2/sqrt(phi^2-1)*(exp((-phi+sqrt(phi^2-1))*w*t)-exp((-phi-sqrt(phi^2-1))*w*t));
y = -(w*(w*exp(-t*w*(phi - (phi^2 - 1)^(1/2)))*(phi - (phi^2 - 1)^(1/2)) - w*exp(-t*w*(phi + (phi^2 - 1)^(1/2)))*(phi + (phi^2 - 1)^(1/2))))/(2*(phi^2 - 1)^(1/2));

xminus = -(w/2/sqrt(phi^2-1)*(exp((-phi+sqrt(phi^2-1))*w*t)-exp((-phi-sqrt(phi^2-1))*w*t)));
yminus = (w*(w*exp(-t*w*(phi - (phi^2 - 1)^(1/2)))*(phi - (phi^2 - 1)^(1/2)) - w*exp(-t*w*(phi + (phi^2 - 1)^(1/2)))*(phi + (phi^2 - 1)^(1/2))))/(2*(phi^2 - 1)^(1/2));


plot(ax,[xminus,flip(x)],[yminus,flip(y)],'color','r');

%{
plot(ax,xminus,yminus,'color','r');
hold on
plot(ax,x,y,'color','r');
hold off
%}

set(ax,'XAxisLocation','origin','XAxisLocation','origin','YAxisLocation','origin','XLim',[-4,4],'YLim',[-70,70]);

xlabel(ax,'\it x','FontSize',20,'Interpreter','tex');

%drawnow

end

