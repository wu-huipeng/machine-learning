# Clustering
----

### Kmeans：基于距离的算法
1. 假设将数据分为k类，随机初始化k个点作为样本中心点。
2. 计算样本数据中每个点离k个样本中心点的距离，将其分配给离他最近的那个样本中心点。
3. 求每一个样本中心点所分配点的平均值，将平均值作为新的样本中心点。
4. 循环操作2,3两步，直到样本中心点不发生太大变化为止或者训练结束。
----
### DBSCAN：基于密度的算法
相关基础概念
---
1. E领域：以该点为圆心，以R为半径的圆
2. 核心对象：在该点的E领域内，最少存在minpts个点。
---
1. 初始化一个点，半径R，最少点minpts。
2. 计算该点的E领域内的点的个数。
3. 如果大于等于minpts，则设置该点为核心对象，并将E领域内的点归属于这个点，继续这些新的点作为新的初始化点，继续进行步骤二，三；否则结束这次循环。
4. 继续在未被归类的点初始化一个点，进行步骤二，三，知道所有的点被归类。
