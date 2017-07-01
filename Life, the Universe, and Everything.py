'''Find the Answer to Life, the Universe, and Everything. 
More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42'''
while 1: 
    num = int(raw_input()) 

    if num == 42: 
        break 
    else: 
        print num
