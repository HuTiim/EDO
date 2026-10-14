import numpy as np
__all__=["euler"]

def euler(fun,tempos,y0):
    '''
    Resolução Edos via método de Euler

    input
    fun
    y0
    t_eval

    output
    y
    '''

    
    y = [y0]

    dt = tempos[1] - tempos[0] 
    
    for t in tempos[:-1]:
        y.append(y[-1] + fun(t,y[-1]) * dt)

    return np.array(y)