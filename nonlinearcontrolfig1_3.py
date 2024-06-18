import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,100)

a = 0.1

x1 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

a = 0.7

x2 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

a = 1.2

x3 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

a = -0.1

x4 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

a = -0.3

x5 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

a = -1.5

x6 = a * np.exp(-t) / (1 - a + a * np.exp(-t))

plt.plot(t,x1,color = 'red',label = 'a = 0.1')

plt.plot(t,x2,color = 'blue',label = 'a = 0.7')

plt.plot(t,x3,color = 'magenta',label = 'a = 1.2')

plt.plot(t,x4,color = 'black',label = 'a = -0.1')

plt.plot(t,x5,color = 'cyan',label = 'a = -0.7')

plt.plot(t,x6,color = 'green',label = 'a = -1.5')

#设置坐标轴线位置
plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines.bottom.set_position(('data',0))

#设置坐标轴线spine脊线的可见性
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

#设置坐标轴刻度
plt.gca().set_xticks([0,1,2,3,4,5,6])
plt.gca().set_yticks([-1,-0.5,0,0.5,1])

#设置坐标轴的字体字号
plt.gca().set_xticklabels(['0','1','3','3','4','5','6'],fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'fontsize':12,
'verticalalignment':'top',
'horizontalalignment':'center'})

plt.gca().set_yticklabels(['-1','-0.5','0','0.5','1'],fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'fontsize':12,
'verticalalignment':'top',
'horizontalalignment':'center'})

#设置坐标标签
plt.xlabel('t',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})

#设置坐标轴刻度
#plt.gca().set_yticks([-2,-1,2,0,1,2])

#设置坐标轴的字体字号
##plt.gca().set_xticklabels(['-2','-1','0','1','2'],fontdict = {'fontfamily':'Times New Roman','fontsize':12,
##'fontweight':'normal',
##'fontstyle':'italic',
##'fontsize':12,
##'verticalalignment':'top',
##'horizontalalignment':'center'})

plt.ylabel('x(t)',fontdict = {'fontfamily':'Times New Roman','fontsize':12,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'center',
'horizontalalignment':'center'})



#使用latex设置标题
plt.gca().set_title(r'x(t)=$\frac{ae^{-t}}{1-a+ae^{-t}}$',fontdict = {'fontfamily':'Times New Roman','fontsize':16,
'fontweight':'normal',
'fontstyle':'italic',
'color':'red',
'verticalalignment':'bottom',
'horizontalalignment':'center'})

#plt.gca().set_aspect('equal')

plt.legend()

plt.show()
