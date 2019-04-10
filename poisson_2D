import numpy


def poisson2D(nx=50, ny=50, nt=150, xmin=0, xmax=1, ymin=0, ymax=1):
    
    dx = (xmax - xmin) / (nx - 1)
    dy = (ymax - ymin) / (ny - 1)
    
    
    p  = numpy.zeros((ny, nx))
    pd = numpy.zeros((ny, nx))
    b  = numpy.zeros((ny, nx))
    
    b[int(ny/4), int(nx/4)] = 100
    b[int(3*ny/4), int(3*nx/4)] = -100
    for it in range(nt):
    
        pd = p.copy()
        
        p[1:-1,1:-1] = (((pd[1:-1,2:]+pd[1:-1,:-2]) * dy**2 +
                          (pd[2:,1:-1]+pd[:-2,1:-1]) * dx**2 -
                          b[1:-1,1:-1] * dy**2 * dx**2) / 
                          (2*(dx**2+dy**2)))
        
        p[:,0]    = 0
        p[:,nx-1] = 0
        p[0,:]    = 0
        p[ny-1,:] = 0
    
    return(p)
