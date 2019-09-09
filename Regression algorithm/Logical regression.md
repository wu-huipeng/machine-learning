# 逻辑回归
---
1. sigmoid函数：<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\frac{1}{1&plus;e^{-x}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\frac{1}{1&plus;e^{-x}}" title="f(x) = \frac{1}{1+e^{-x}}" /></a>

2. 线性方程： <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;w&space;*&space;x&space;&plus;&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;w&space;*&space;x&space;&plus;&space;b" title="y = w * x + b" /></a>

3. 输出方程： <a href="https://www.codecogs.com/eqnedit.php?latex=h(x)&space;=&space;f(y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h(x)&space;=&space;f(y)" title="h(x) = f(y)" /></a>

4. 输入x分类为1的概率：<a href="https://www.codecogs.com/eqnedit.php?latex=P(y=1|x;w)&space;=&space;h(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y=1|x;w)&space;=&space;h(x)" title="P(y=1|x;w) = h(x)" /></a>

5. 对应分类为0的概率：<a href="https://www.codecogs.com/eqnedit.php?latex=P(y=0|x;w)&space;=&space;1&space;-&space;h(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y=0|x;w)&space;=&space;1&space;-&space;h(x)" title="P(y=0|x;w) = 1 - h(x)" /></a>

6. 后验概率： <a href="https://www.codecogs.com/eqnedit.php?latex=P(y|x;w)&space;=&space;h(x)^{y}*(1-h(x))^{1-y}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y|x;w)&space;=&space;h(x)^{y}*(1-h(x))^{1-y}" title="P(y|x;w) = h(x)^{y}*(1-h(x))^{1-y}" /></a>

7. 对数似然函数：<a href="https://www.codecogs.com/eqnedit.php?latex=l(w)&space;=&space;\sum&space;y*log~h(x)&space;&plus;&space;(1-y)*log~(1-h(x))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?l(w)&space;=&space;\sum&space;y*log~h(x)&space;&plus;&space;(1-y)*log~(1-h(x))" title="l(w) = \sum y*log~h(x) + (1-y)*log~(1-h(x))" /></a>

8. 目标函数J,最大化对数似然函数对应着最小化J：<a href="https://www.codecogs.com/eqnedit.php?latex=J(w)&space;=&space;-l(w)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(w)&space;=&space;-l(w)" title="J(w) = -l(w)" /></a>

9. J对w求导: <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;J}{\partial&space;w}&space;=&space;-1*(y-f(x))*x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;J}{\partial&space;w}&space;=&space;-1*(y-f(x))*x" title="\frac{\partial J}{\partial w} = -1*(y-f(x))*x" /></a>

10. J对b求导：<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;J}{\partial&space;b}&space;=&space;-1*(y-f(x))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;J}{\partial&space;b}&space;=&space;-1*(y-f(x))" title="\frac{\partial J}{\partial b} = -1*(y-f(x))" /></a>

11. 代价函数：<a href="https://www.codecogs.com/eqnedit.php?latex=loss&space;=&space;\sum&space;(y&space;-&space;f(w*x&plus;b))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?loss&space;=&space;\sum&space;(y&space;-&space;f(w*x&plus;b))^2" title="loss = \sum (y - f(w*x+b))^2" /></a>

12.利用梯度下降算法不断更新w，b，直到代价函数小于某一个阈值或者直到训练结束。
