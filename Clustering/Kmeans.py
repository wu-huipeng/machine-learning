## 版本一
from sklearn.datasets import load_iris
import numpy as np


a,b = load_iris(return_X_y=True)

x = a[:,:2]   #便于绘图

center_1 = np.array([5,3.5])   #初始化中心点
center_2 = np.array([6,2]) 
center_3 = np.array([7,3])

for k in range(200):
    center_list1 = []
    center_list2 = []
    center_list3 = []
    for i in x:
        a = ((i[0] - center_1[0])*(i[1]-center_1[1]))**2
        b = ((i[0] - center_2[0])*(i[1]-center_2[1]))**2
        c = ((i[0] - center_3[0])*(i[1]-center_3[1]))**2

        if a<b and a<c :
            center_list1.append(i)
        elif b<c:
            center_list2.append(i)
        elif c<b :
            center_list3.append(i)
    new_1_x =  0
    new_1_y = 0

    for a in center_list1:
        new_1_x +=a[0]
        new_1_y +=a[1]
    center_1[0] = new_1_x / (len(center_list1))
    center_1[1] = new_1_y / (len(center_list1))

    new_1_x = 0
    new_1_y = 0
    for a in center_list2:
        new_1_x += a[0]
        new_1_y += a[1]
    print(len(center_list3))
    center_2[0] = new_1_x / (len(center_list2))
    center_2[1] = new_1_y / (len(center_list2))

    new_1_x = 0
    new_1_y = 0
    for a in center_list3:
        new_1_x += a[0]
        new_1_y += a[1]
    center_3[0] = new_1_x / (len(center_list3))
    center_3[1] = new_1_y / (len(center_list3))
    
# 版本二    学习于https://www.cnblogs.com/zxzhu/p/7994612.html
import numpy as np
from sklearn.datasets import make_blobs

def Distance(x):
    def Dis(y):
        return np.sqrt(sum((x - y) ** 2))

    return Dis


def init_k_means(k):
    k_means = {}
    for i in range(k):
        k_means[i] = []
    return k_means


def cal_seed(k_mean):
    k_mean = np.array(k_mean)
    new_seed = np.mean(k_mean, axis=0)
    return new_seed


def K_means(data, seed_k, k_means):
    for i in data:
        f = Distance(i)
        dis = list(map(f, seed_k))
        index = dis.index(min(dis))
        k_means[index].append(i)
    new_seed = []
    for i in range(len(seed_k)):
        new_seed.append(cal_seed(k_means[i]))
    new_seed = np.array(new_seed)
    return k_means, new_seed


def run_K_means(data, k):
    seed_K = data[np.random.randint(len(data), size=k)]
    k_means = init_k_means(k)
    result = K_means(data, seed_K, k_means)
    count = 0
    while not (result[1] == seed_K).all():
        count += 1
        seed_k = result[1]
        k_means = init_k_means(k=7)
        result = K_means(data, seed_k, k_means)
        
 ## sklearn API
from sklearn.cluster import KMeans   #导入模型
from sklearn.datasets import load_iris  #导入数据


x,y = load_iris(return_X_y=True)

kmean = KMeans().fit(x)    #训练模型

print(kmean.labels_)     #打印聚类结果


