import numpy as np
import math
import random
from sklearn.datasets import make_circles
#记录那些点是遍历过的，那些点是未遍历过的
class visited():
    def __init__(self,count=0):
        self.visitedlist = []
        self.unvisitedlist = [i for i in range(count)]
        self.unvisitednum = count
    def visited(self,p):
          self.visitedlist.append(p)
          self.unvisitedlist.remove(p)
          self.unvisitednum -= 1
          
def Distance(x,y):
    return np.sqrt(np.power(x-y,2).sum())
  
def DBSCAN(data,eps,minpts):   #eps E领域，领域内的最小个数
      count = data.shape[0]
      visite = visited(count)
      C = [0 for i in range(count)]
      k = -1
      
      while(visite.unvisitednum>0):
          p = random.choice(visite.unvisitedlist)   #随机初始化一个点
          visite.visited(p)
          N = [i for i in visite.unvisitedlist if Distance(data[p],data[i])<=eps]    #计算E领域内的点
          if (len(N)>=minpts):
              k += 1
              C[p] = k
              
              for p1 in N:
                  visite.visited(p1)
                  M = [i for i in visite.unvisitedlist if Distance(data[p1],data[i])<=eps]
                  
                  if (len(M)>=minpts):    #如果为核心点，则将在他领域内的点都加入其中
                      for i in M:
                          if i is not in N:
                              N.append(i)
                  C[p1] = k      
          else:
            C[p] = -1     #标记为异常点
      return C
    
x ,y = make_circles(n_samples=2500,factor=0.5,noise=0.15,random_state=42)

a = DBSCAN(x,0.1,10)

print(a)

##  sklearn API
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles

x,y = make_circles(n_samples=2550)

a = DBSCAN(eps=0.1,min_samples=10)

a.fit(x)

pred = a.labels_

print(pred)  
print(y)

          
