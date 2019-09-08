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
