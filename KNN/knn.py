from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter


x , y = make_classification(n_samples=1000,n_features=10,n_classes=4,n_clusters_per_class=2,n_informative=3)

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=123)



class KNN():

    def __init__(self,n_nearest=5):
        self.n_nearest = n_nearest

    def fit(self,x_train,y_train):
        self.x= x_train
        self.y = y_train

    def predict(self,xs):
        if xs.ndim >= 2:
            pred = []
            for x in xs:
                distance = np.sqrt(np.sum((self.x-x)**2,axis=1))
                nearest = distance.argsort()[:self.n_nearest]
                a = Counter(np.take(self.y,nearest))
                y_pred = a.most_common(1)[0][0]
                pred.append(y_pred)
            return np.array(pred)
        else:
            distance = np.sqrt(np.sum((self.x - xs) ** 2, axis=1))
            nearest = distance.argsort()[:self.n_nearest]
            a = Counter(np.take(self.y, nearest))
            y_pred = a.most_common(1)[0][0]
            return y_pred


a = KNN(15)

a.fit(x_train,y_train)

pred = a.predict(x_test[100])

t_pred = a.predict(x_test[:100])
