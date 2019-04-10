import numpy
from matplotlib import pyplot, cm


def plot2D(x=numpy.linspace(0,1,50), y=numpy.linspace(0,1,50), f=[[1]*50]*50):
    fig = pyplot.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, f, rstride=1, cstride=1, cmap=cm.viridis,
                           linewidth=0, antialiased=False)
    ax.view_init(30, 225)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
