
import numpy as np
import pandas as pd

def fila_cuatro(a,b,c,d):
    
    dict_aux = {
        'col1' : [a,b,c,d]
    }
    
    df_aux = pd.DataFrame(dict_aux)

    return df_aux

fun_test = fila_cuatro(1,2,3,4)
print(fun_test)

