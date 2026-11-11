def number_pattern(n):
    numbers_list = ''
    if isinstance(n,int) == True:
        if n > 0:
            for num in range(1,n+1):
                numbers_list += str(num)
                numbers_list += ' '
            return(numbers_list.strip())
        else: return("Argument must be an integer greater than 0.")
    else:
        return("Argument must be an integer value.")

print(number_pattern(4))
