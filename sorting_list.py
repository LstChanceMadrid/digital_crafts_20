list1 = [5, 6, 3, 7, 9, 8, 5, 8]
print(len(list1))



def sort_ascending(list1):
    ascending_order = []

    while list1:
        minimum = list1[0]
        for number in list1:
            if (number < minimum):
                minimum = number
        ascending_order.append(minimum)
        list1.remove(minimum)
    print(ascending_order)
    return ascending_order
    
        
        

def sort_descending(list1):
    descending_order = []

    while list1:
        maximum = list1[0]
        for number in list1:
            if (number > maximum):
                maximum = number
        descending_order.append(maximum)
        list1.remove(maximum)

    print(descending_order)
    return descending_order




#sort_ascending(list1)

#sort_descending(list1)


