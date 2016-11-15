import matplotlib.pyplot as plt


def plotData(x,y):
    plt.figure(1)
    plt.plot(x,y,'ro')
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    
