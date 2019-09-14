import Mass_calc as Mc
import matplotlib.pyplot as plt
import numpy as np


def main():
    A = 235
    Z = 89
    N_atomic = list() 
    Masses_real = list()
    for i in range(8):
        Masses_real.append(Mc.Nucleon(Z+i,A).Calculate_Mass())
        N_atomic.append(Z+i)
    
    evenZ = np.array(N_atomic)[[0,2,4,6]]
    oddZ = np.array(N_atomic)[[1,3,5,7]]
    evenM = np.array(Masses_real)[[0,2,4,6]]
    oddM = np.array(Masses_real)[[1,3,5,7]]
    z1 = np.polyfit(evenZ, evenM, 3)
    f1 = np.poly1d(z1)
    z2 = np.polyfit(oddZ, oddM, 3)
    f2 = np.poly1d(z2)
    x_new = np.linspace(N_atomic[0], N_atomic[-1], 50)
    y_new1 = f1(x_new)
    y_new2 = f2(x_new)


    plt.scatter(N_atomic,Masses_real,c='Red')
    plt.plot(x_new, y_new1)
    plt.plot(x_new, y_new2)
    plt.show()
    # x_new = np.linspace(x[0], x[-1], 50)
    # y_new = f(x_new)
    


if __name__ == "__main__":
    main()