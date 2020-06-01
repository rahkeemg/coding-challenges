def hex_string_to_RGB(hex_string): 
    '''
      This function assumes that the parameter hex_string begins with # and 
      is followed by 6 hexadecimal characters in [0,E]
    '''
    color = 'rgb' #setup the colors character
    string = hex_string.strip('#') #remove # charracter from hex string
    
    # group into 3 sets of 2
    vals = [int(string[i:i + 2], 16) for i in range(0, len(string), 2)]

    return dict(zip(color, vals))