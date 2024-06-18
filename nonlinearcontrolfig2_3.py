#应用非线性控制图2.3一阶系统相图
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
 
x = np.linspace(-3,3,100)

y = lambda x:x**3 - 4 * x

plt.plot(x,y(x))



#创建沿图形的箭头
plt.arrow(1, y(1), -0.5, 1, shape = 'full', length_includes_head=True, head_width=0.35, color = 'red')

plt.arrow(-1, y(-1), 0.5, -1, shape = 'full', length_includes_head=True, head_width=0.35, color = 'red')

plt.arrow(2.5, y(2.5), 0.2, 0.2 * (3 * 2.5 **2 - 4), shape = 'full', length_includes_head=True, head_width=0.35, color = 'red')

plt.arrow(-2.5, y(-2.5), -0.2, -0.2 * (3 * 2.5 **2 - 4), shape = 'full', length_includes_head=True, head_width=0.35, color = 'red')

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

plt.gca().set_ylabel(r'$\frac{ dx }{ dt }$',\
fontdict = {'fontfamily':'Times New Roman',\
            'fontsize':20,'fontweight':'normal',\
            'fontstyle':'italic',\
            'color':'red',\
            'verticalalignment':'center',\
            'horizontalalignment':'center'},loc = 'top')

plt.xticks(np.linspace(-5,5,11))

plt.gca().set_xticks(np.linspace(-5,5,21))

plt.gca().set_xticklabels(['-5','-4.5','-4','-3.5','-3','-2.5','-2','-1.5','-1',\
                           '-0.5','0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5'])

plt.show()
