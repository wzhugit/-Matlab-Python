#linear phase analysis线性系统相图分析
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,50,1000)

#稳定节点情况---线性系统含有2个负实根
x = np.exp(-3*t) - 5 * np.exp(-5*t)

fig = plt.figure()

ax1 = fig.add_subplot(3,2,1)

plt.plot(x,-3 * np.exp(-3 * t) + 25 * np.exp(-5 * t))

plt.title('Stable Nodes---linear system with 2 nagative real roots')

#设置坐标轴线位置
ax1.spines['left'].set_position(('data',0))

ax1.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax1.spines['right'].set_visible(False)

ax1.spines['top'].set_visible(False)

ax1.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax1.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax1.set_aspect('equal')

#不稳定节点情况---线性系统含有2个正实根
x = np.exp(3*t) + 3 * np.exp(5*t)

ax2 = fig.add_subplot(3,2,2)

plt.plot(x,3 * np.exp(3 * t) + 15 * np.exp(5 * t))

plt.title('UnStable Nodes\n---linear system with 2 positive real roots')

#设置坐标轴线位置
ax2.spines['left'].set_position(('data',0))

ax2.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax2.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)

ax2.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax2.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax2.set_aspect('equal')

#鞍点情况---线性系统含有一对互为相反数的实根
x = np.exp(3*t) + 3 * np.exp(-3*t)

ax3 = fig.add_subplot(3,2,3)

plt.plot(x,3 * np.exp(3 * t) - 9 * np.exp(-3 * t))

plt.title('Saddle Points\n---linear system with 2 opposite real roots with same absolute value')

#设置坐标轴线位置
ax3.spines['left'].set_position(('data',0))

ax3.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax3.spines['right'].set_visible(False)

ax3.spines['top'].set_visible(False)

ax3.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax3.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax3.set_aspect('equal')

#稳定焦点情况---线性系统含有一对负实部共轭复根
x = np.exp(-3*t)*(np.cos(5*t)+2*np.sin(5*t))

ax4 = fig.add_subplot(3,2,4)

plt.plot(x,np.exp(-3*t)*(10*np.cos(5*t) - 5*np.sin(5*t)) - 3*np.exp(-3*t)*(np.cos(5*t) + 2*np.sin(5*t)))

plt.title('Stable Focus\n---linear system with a couple of conjugate complex roots')

#设置坐标轴线位置
ax4.spines['left'].set_position(('data',0))

ax4.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax4.spines['right'].set_visible(False)

ax4.spines['top'].set_visible(False)

ax4.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax4.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax4.set_aspect('equal')

#不稳定焦点情况---线性系统含有一对正实部共轭复根
ax5 = fig.add_subplot(3,2,5)

x = np.exp(3 * t) * (np.cos(5 * t)+2 * np.sin(5 * t))

plt.plot(x,np.exp(3*t)*(10*np.cos(5*t) - 5*np.sin(5*t)) + 3*np.exp(3*t)*(np.cos(5*t) + 2*np.sin(5*t)))

plt.title('UnStable Focus\n---linear system with a couple of conjugate complex roots')

#设置坐标轴线位置
ax5.spines['left'].set_position(('data',0))

ax5.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax5.spines['right'].set_visible(False)

ax5.spines['top'].set_visible(False)

ax5.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax5.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax5.set_aspect('equal')

#中心点情况---线性系统含有一对共轭纯虚根
ax6 = fig.add_subplot(3,2,6)

x = np.cos(5 * t)+2 * np.sin(5 * t)

plt.plot(x,-5 * np.sin(5 * t) + 10 * np.cos(5 * t))

plt.title('Center Point\n---linear system with a couple of pure conjugate imagine roots')

#设置坐标轴线位置
ax6.spines['left'].set_position(('data',0))

ax6.spines.bottom.set_position(('data',0))

#设置坐标轴线(spine脊线：标注数据区域的边界)可见性
ax6.spines['right'].set_visible(False)

ax6.spines['top'].set_visible(False)

ax6.set_xlabel('x',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax6.set_ylabel(r'$\dot{x}$',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

ax6.set_aspect('equal')

plt.show()
