array = [5, 6, 3, 7, 9, 8, 5, 8]
print(len(array))



def sort_ascending(array):
    ascending_order = []

    while array:
        minimum = array[0]
        for number in array:
            if (number < minimum):
                minimum = number
        ascending_order.append(minimum)
        array.remove(minimum)
    print(ascending_order)
    return(ascending_order)
    
        
        

def sort_descending(array):
    descending_order = []

    while array:
        maximum = array[0]
        for number in array:
            if (number > maximum):
                maximum = number
        descending_order.append(maximum)
        array.remove(maximum)

    print(descending_order)
    return descending_order




sort_ascending(array)

sort_descending(array)


