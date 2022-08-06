from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from interpulation import divided_diff,newton_poly, newton_polynomial



def generate_data_points(n : int):
    x = np.zeros([n-1])
    y = np.zeros([n-1])
    for i in range(1,n):
        xi = -5 + (10*(i-1))/(n-1)
        yi = 1/(xi**2+1)
        x[i-1]=xi
        y[i-1]=yi
    return x,y



def main():
    fig, ax = plt.subplots()
    newx = np.arange(-20,20,0.1)

    n = [100]
    fx = 1/(1+newx**2)
    for i in iter(n): 
        print(i)
        x,y = generate_data_points(i)
        newy = newton_polynomial(x,y,newx)
        
        plt.scatter(x,y)
        ax.plot(newx,newy, label='n={0}'.format(i))
        ax.plot(newx,fx)
        legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
        legend.get_frame().set_facecolor('C0')
        plt.show()


main()