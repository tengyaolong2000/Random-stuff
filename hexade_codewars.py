def rgb(r, g, b):
    list = ['r', 'g', 'b']

    
    if r > 255:
        list[0] = 'FF'
    
    elif r < 0:
        list[0] = '00'

    else:
        list[0] = hex(r).upper().replace('0X', '')
    
    if g > 255:
        list[1] = 'FF'
    
    elif g < 0:
        list[1] = '00'

    else:
        list[1] = hex(g).upper().replace('0X', '')
    
    if b > 255:
        list[2] = 'FF'
    
    elif b < 0:
        list[2] = '00'

    else:
        list[2] = hex(b).upper().replace('0X', '')
    
    
        
        

    for n in range(0,3):
        if len(list[n]) == 1:
            list[n] = '0' + list[n]


    list = ''.join(list)
    return list







