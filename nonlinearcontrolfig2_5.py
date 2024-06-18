#应用非线性控制图2.5卫星控制系统相图
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

U = 4

y = np.linspace(-2,2,100)

x1left = lambda y:(y**2 - 4) / (2 * U)

x2left = lambda y:(y**2 - 3) / (2 * U)

x3left = lambda y:(y**2 + 2) / (2 * U)

x1right = lambda y:(y**2 - 4) / (- 2 * U)

x2right = lambda y:(y**2 - 3) / (- 2 * U)

x3right = lambda y:(y**2 + 2) / (- 2 * U)

plt.subplot(1,3,1)

plt.plot(x1left(y),y)

plt.plot(x2left(y),y)

plt.plot(x3left(y),y)

#创建沿图形的箭头
plt.arrow(x1left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x2left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x3left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines.bottom.set_position(('data',0))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#plt.gca().set_aspect('equal')
plt.gca().set_xlabel('x',fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'right')

plt.gca().set_ylabel(r'$\dot{ x }$',\
fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'top')

plt.gca().annotate(r'$\it{u} = \it{U}$',(-0.5,1.5))

plt.subplot(1,3,2)

plt.plot(x1right(y),y)

plt.plot(x2right(y),y)

plt.plot(x3right(y),y)

#创建沿图形的箭头
plt.arrow(x1right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x2right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x3right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines.bottom.set_position(('data',0))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#plt.gca().set_aspect('equal')
plt.gca().set_xlabel('x',fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'right')

plt.gca().set_ylabel(r'$\dot{ x }$',\
fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'top')

plt.gca().annotate(r'$\it{u} = -\it{U}$',(0.5,1.5))

plt.subplot(1,3,3)

plt.plot(x1left(y),y)

plt.plot(x2left(y),y)

plt.plot(x3left(y),y)

#创建沿图形的箭头
plt.arrow(x1left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x2left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x3left(1), 1, 0.05, U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines.bottom.set_position(('data',0))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#plt.gca().set_aspect('equal')
plt.gca().set_xlabel('x',fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'right')

plt.gca().set_ylabel('$\it\dot{ x }$',\
fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'top')

plt.gca().annotate(r'$\it{u} = \it{U}$',(-0.5,1.5))

plt.plot(x1right(y),y)

plt.plot(x2right(y),y)

plt.plot(x3right(y),y)

#创建沿图形的箭头
plt.arrow(x1right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x2right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.arrow(x3right(-1), 1, 0.05, -U/1*0.05, shape = 'full', length_includes_head=True, head_width=0.05, color = 'red')

plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines.bottom.set_position(('data',0))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#plt.gca().set_aspect('equal')
plt.gca().set_xlabel('x',fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'right')

plt.gca().set_ylabel('$\dot{ x }$',\
fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'top')

plt.gca().annotate(r'$\it{u} = -\it{U}$',(0.5,1.5))

plt.show()
