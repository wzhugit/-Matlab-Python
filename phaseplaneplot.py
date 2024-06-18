#相平面图
import numpy as np
import matplotlib.pyplot as plt

#x,y = np.meshgrid(np.linspace(-10,10,50),np.linspace(-10,10,50))
x,y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))

u = y

v = -(x**2 + 3*x + 0.6*y)

plt.streamplot(x,y,u,v)

plt.gca().spines['left'].set_position(('data',0))

plt.gca().spines.bottom.set_position(('data',0))

plt.gca().spines['right'].set_visible(False)

plt.gca().spines['top'].set_visible(False)

plt.gca().set_aspect('equal')

plt.gca().set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':20,'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'},loc = 'right')

plt.gca().set_ylabel(r'$\frac{ dx }{ dt }$',fontdict = {'fontfamily':'Times New Roman','fontsize':20,'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'},loc = 'top')

plt.show()
