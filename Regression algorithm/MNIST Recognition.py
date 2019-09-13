## sklearn API 实现
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('MNIST.csv')    #读取数据

label = data['label'].values     #得到标签

x = data.loc[:,data.columns !='label'].values.astype(np.float32)    #得到图片
x = x / 255.0    #归一化  

x_train , x_test ,y_train, y_test = train_test_split(x,label,random_state=123)

model = LogisticRegression(multi_class='auto',solver='lbfgs')   #构造模型
 
model.fit(x_train,y_train)   #训练模型

print(model.score(x_test,y_test))   #打印模型在测试集上的分数



#手写算法实现
