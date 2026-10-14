import numpy as np
__all__=["euler"]

def euler(fun,tempos,y0):
    
    y = [y0]

    dt = tempos[1] - tempos[0] 
    
    for t in tempos[:-1]:
        y.append(y[-1] + fun(t,y[-1]) * dt)

    return np.array(y)