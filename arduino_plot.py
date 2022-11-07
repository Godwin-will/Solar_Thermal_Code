from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as pd

# See Matplotlib Tutorial (Part 9): Plotting Live Data in Real-Time 
# https://www.youtube.com/watch?v=Ercd-Ip5PfQ
# Data points are created by th arduino.py script (needs to run in parallel)

points = 600    # number of data points to plot

def animate(i, points):
    '''
    Retrieves data from the data.csv file and creates a live plot.
    '''
    data = pd.read_csv('data.csv', header=None, index_col=0)
    data.index = pd.to_datetime(data.index)
    data = data.astype(float)

    x = data.index[-points:]
    y1 = data[1][-points:]
    y2 = data[2][-points:]
    y3 = data[3][-points:]
    y4 = data[4][-points:]
    plt.cla()
    plt.plot(x, y1, label='Channel 1')
#    plt.plot(x, y2, label='Channel 2')
#    plt.plot(x, y3, label='Channel 3')
#    plt.plot(x, y4, label='Channel 4')
    plt.legend()
ani = FuncAnimation(plt.gcf(), animate, fargs=(points,))
plt.show()