## 最小二成法求解

import matplotlib.pyplot as plt

def main():
    x = [1,2,3,4,5,6,7,8,9]
    y = [1.1,2.5,3.2,4.6,5.1,5.4,6.7,6.7,8.1]
    x_sum = 0
    y_sum = 0
    x2_sum = 0
    y2_sum = 0
    for i in range(len(x)):
        x_sum += x[i]
        y_sum += y[i]
        x2_sum += x[i]*x[i]
        y2_sum += y[i]*y[i]
    x_mean = x_sum / float(len(x))
    y_mean = y_sum / float(len(y))
    x_y_sum = 0
    for i in range(len(x)):
        x_y_sum += y[i] *(x[i] - x_mean)
    w = x_y_sum / (x2_sum - (1.0/len(x)) * x_sum * x_sum)
    b = y_mean -w * x_mean
    y_pred = []
    for i in x:
        y_pred.append(w*i+b)
    plt.scatter(x,y)
    plt.plot(x,y_pred)
    plt.show()
if __name__ == '__main__':
    main()

    
## 梯度下降法求解
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 样本x
y = [1.1, 2.5, 3.2, 4.6, 5.1, 5.4, 6.7, 6.7, 8.1]  # 样本y
#   拟和方程为： y = 0.8*x + 0.8
w = 5    #随机初始化w
b = 3      #随机初始化b
loss = 0

for i in range(1000):    #更新w，b的次数
    if loss < 0.001:
        break
    w_D = 0
    b_D = 0
    loss = 0
    for a in range(len(x)):
        loss += (y[a] - (w*x[a]+b))**2    


        w_D -=(y[a]-(w*x[a]+b))*x[a]   #得到函数对w的偏导数值
        b_D +=w*x[a] + b - y[a]          #得到函数对b的偏导数值
    print('loss:%.2f'%loss)

    w = w - 0.002*w_D     #更新w   0.002为学习率
    b = b - 0.002*b_D     #更新b

    print('w:%.2f'%w)
    print('b:%.2f'%b)
    
## sklearn实现

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

x , y = make_regression(n_samples=5000,n_features=10,random_state=42)

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=123)


linear = LinearRegression()

linear.fit(x_train,y_train)

y_pred = linear.predict(x_test)

loss = np.sum((y_test - y_pred)**2)   
print(loss)
