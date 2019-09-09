# 线性回归-最小二乘法
----

### 目标方程： <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;w&space;*&space;x&space;&plus;&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;w&space;*&space;x&space;&plus;&space;b" title="y = w * x + b" /></a>

### 代价函数：<a href="https://www.codecogs.com/eqnedit.php?latex=E&space;=&space;\frac{1}{2}\sum&space;(y&space;-&space;w&space;*&space;x&space;&plus;&space;b)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E&space;=&space;\frac{1}{2}\sum&space;(y&space;-&space;w&space;*&space;x&space;&plus;&space;b)^2" title="E = \frac{1}{2}\sum (y - w * x + b)^2" /></a>


### 分别对w ， b 求导解的w，b并令其为零：
##### w:<a href="https://www.codecogs.com/eqnedit.php?latex=w&space;=&space;\frac{\sum&space;(x*y)}{(\sum&space;x^2)-\frac{1}{n}*(\sum&space;x)^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w&space;=&space;\frac{\sum&space;(x*y)}{(\sum&space;x^2)-\frac{1}{n}*(\sum&space;x)^2}" title="w = \frac{\sum (x*y)}{(\sum x^2)-\frac{1}{n}*(\sum x)^2}" /></a>
##### b:<a href="https://www.codecogs.com/eqnedit.php?latex=b&space;=&space;\bar{y}&space;-&space;w&space;*\bar{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b&space;=&space;\bar{y}&space;-&space;w&space;*\bar{x}" title="b = \bar{y} - w *\bar{x}" /></a>

### 解出 w ， b 的值即可。

---
# 线性回归梯度下降法
---
### 目标方程： <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;w&space;*&space;x&space;&plus;&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;w&space;*&space;x&space;&plus;&space;b" title="y = w * x + b" /></a>
### 代价函数：  <a href="https://www.codecogs.com/eqnedit.php?latex=E&space;=&space;\frac{1}{2}\sum&space;(y&space;-&space;w&space;*&space;x&space;&plus;&space;b)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E&space;=&space;\frac{1}{2}\sum&space;(y&space;-&space;w&space;*&space;x&space;&plus;&space;b)^2" title="E = \frac{1}{2}\sum (y - w * x + b)^2" /></a>

### 代价函数对w求导：<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;E}{\partial&space;W}&space;=&space;(y-(w*x&plus;b))*x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;E}{\partial&space;W}&space;=&space;(y-(w*x&plus;b))*x" title="\frac{\partial E}{\partial W} = (y-(w*x+b))*x" /></a>

### 代价函数对b求导：<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;E}{\partial&space;b}&space;=&space;w*x&plus;b-y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;E}{\partial&space;b}&space;=&space;w*x&plus;b-y" title="\frac{\partial E}{\partial b} = w*x+b-y" /></a>

### 更新w： <a href="https://www.codecogs.com/eqnedit.php?latex=w\_new&space;=&space;w\_old&space;-&space;\eta&space;*\frac{\partial&space;E}{\partial&space;W}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w\_new&space;=&space;w\_old&space;-&space;\eta&space;*\frac{\partial&space;E}{\partial&space;W}" title="w\_new = w\_old - \eta *\frac{\partial E}{\partial W}" /></a>

### 更新b：<a href="https://www.codecogs.com/eqnedit.php?latex=b\_new&space;=&space;b\_old&space;-&space;\eta&space;*\frac{\partial&space;E}{\partial&space;b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b\_new&space;=&space;b\_old&space;-&space;\eta&space;*\frac{\partial&space;E}{\partial&space;b}" title="b\_new = b\_old - \eta *\frac{\partial E}{\partial b}" /></a>

### 循环更新w， b。当代价函数小于一个阈值时，停止，算法结束。<a href="https://www.codecogs.com/eqnedit.php?latex=\eta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\eta" title="\eta" /></a>为学习率
