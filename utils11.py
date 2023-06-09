import pandas as pd
import numpy as np
from matplotlib import pyplot

# Some functions to plot our points and draw the lines
def plot_points(features, labels):
    X = np.array(features)
    y = np.array(labels)
    galaxy = X[np.argwhere(y=='GALAXY')]
    qso = X[np.argwhere(y=='QSO')]
    star = X[np.argwhere(y=='STAR')]
    pyplot.scatter([s[0][0] for s in galaxy],
                   [s[0][1] for s in galaxy],
                   s = 35,
                   color = 'cyan',
                   edgecolor = 'k',
                   marker = '^')
    pyplot.scatter([s[0][0] for s in qso],
                   [s[0][1] for s in qso],
                   s = 25,
                   color = 'red',
                   edgecolor = 'k',
                   marker = 's')
    pyplot.scatter([s[0][0] for s in star],
               [s[0][1] for s in star],
               s = 25,
               color = 'green',
               edgecolor = 'k',
               marker = 'o')
    pyplot.xlabel(features.keys()[0])
    pyplot.ylabel(features.keys()[1])
    pyplot.legend(['galaxy','qso','star'])
    pyplot.show()

def plot_model(X, y, model):
    X = np.array(X)
    y = np.array(y)
    plot_step = 0.01
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    pyplot.contour(xx, yy, Z,colors = 'k',linewidths = 3)
    plot_points(X, y)
    pyplot.contourf(xx, yy, Z, colors=['red', 'blue'], alpha=0.2, levels=range(-1,2))
    pyplot.show()