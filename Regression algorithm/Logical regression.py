## 源码实现
import matplotlib.pyplot as plt                                                                
import math                                                                                    
                                                                                               
def sigmoid(x):                                                                                
                                                                                               
    a =1.0/(1+ math.exp(-x))                                                                   
    if a>0.5:                                                                                  
        return 1                                                                               
    else:                                                                                      
        return 0                                                                               
                                                                                               
def main():                                                                                    
    x = [0,1,2.1, 2,4.6, 3, 4, 5, 6, 7, 8, 9,10,12,14,15,16,17,21,22,23,24,25,26]  # 样本x       
                                                                                               
    y = [0,0, 0,0, 0,0, 0, 0, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1]  # 样本y  表示类别                 
                                                                                               
    w = 5                           #初始化w，b，                                                   
    b = 3                                                                                      
    loss = 0                                                                                   
                                                                                               
    for i in range(1000):                                                                      
        w_D = 0                                                                                
        b_D = 0                                                                                
        loss = 0                                                                               
        for a in range(len(x)):                                                                
            loss += (y[a] - sigmoid(w*x[a]+b))**2                                              
            w_D += -1*(y[a] - sigmoid(w*x[a]+b)) *x[a]                                         
                                                                                               
            b_D +=  -1*(y[a] - sigmoid(w*x[a]+b))                                              
        print('loss:%.2f'%loss)                                                                
                                                                                               
        w = w - 0.2*(w_D)                                                                      
        b = b - 0.2*(b_D)                                                                      
        print(w_D)                                                                             
        print('w:%.2f'%w)                                                                      
        print('b:%.2f'%b)                                                                      
                                                                                               
    a = sigmoid(w *7+ b)                                                                       
    print("%.2f"%a)                                                                            
if __name__ == '__main__':                                                                     
    main()    

### sklearn实现

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x , y = make_classification(n_samples=5000,n_features=20,random_state=123)

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=123)

linear = LogisticRegression()

linear.fit(x_train,y_train)

y_pred = linear.predict(x_test)

print(y_pred[:20])
print(y_test[:20])
