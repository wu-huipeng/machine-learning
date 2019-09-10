from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split



x , y  = make_classification(n_samples=1000,n_features=40,random_state=42)  #构造数据

x_train, x_test ,y_train ,y_test = train_test_split(x,y,random_state=42)    #划分数据


knn = KNeighborsClassifier()   #构建模型

knn.fit(x_train,y_train)      #训练

pred = knn.predict(x_test)    #预测值

score = knn.score(x_test,y_test)   #测试分数

print(score)   #score = 0.76

