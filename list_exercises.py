array = [4, 6, 7, 2, 3, 0, -1]
integer = 2
vector_one = [3, 4, 5, 6, 2, -12]
vector_two = [1, 0, -1, 5, 6, 1]

#Sum the Numbers

def sum_of_numbers(array):
    sum = 0
    for number in array:
        sum += number
    print("Sum")
    print(sum)

sum_of_numbers(array)

#Largest Number

def largest_integer(array):
    maximum = array[0]
    for number in array:
        if (number > maximum):
            maximum = number
    print("Maximum")
    print(maximum)

largest_integer(array)
                


#Smallest Number

def smallest_integer(array):
    minimum = array[0]
    for number in array:
        if (number < minimum):
            minimum = number
    print("Minimum")
    print(minimum)

smallest_integer(array)

#Even Numbers

def even_integers(array):
    print("Even")
    for number in array:
        if (number % 2 == 0):
            print(number)

even_integers(array)

#Positive Numbers

def positive_integers(array):
    print("Positive")
    for number in array:
        if (number > 0):
            print(number)

positive_integers(array)

#Positive Numbers II

def positive_list(array):
    print("Positive List")
    positive_list = []
    for number in array:
        if (number % 2 == 0):
            positive_list.append(number)
    print(positive_list)

positive_list(array)


#Multiply a list

def multiply_list(array, integer):
    print("Multiply List")
    multiply_list = []
    for number in array:
        result = 0
        result = number * integer
        multiply_list.append(result)
    print(multiply_list)

multiply_list(array, integer)


#Multiply Vectors

def multiply_vectors(vector_one, vector_two):
    print("Multiply Vectors")
    multiply_vectors_list = []
    i = 0
    for number in vector_one:
        result = 0
        result = vector_one[i] * vector_two[i]
        i += 1
        multiply_vectors_list.append(result)
    print(multiply_vectors_list)

multiply_vectors(vector_one, vector_two)


#Matrix Addition & Matrix Addition II

matrix_one = [[1, 2], [3, 4]]
matrix_two = [[5, 6], [7, 8]]

def matrix_addition(matrix_one, matrix_two):
    print("Matrix Addition")
    matrix_addition_list = []
    i = 0
    n = 0
    for index in matrix_one:
        matrix_addition_number = []
        n = 0
        for number in index:
            result = 0
            result = int(matrix_one[i][n]) + int(matrix_two[i][n])
            n += 1
            matrix_addition_number.append(result)
        i += 1

        matrix_addition_list.append(matrix_addition_number)
    print(matrix_addition_list)
    


matrix_addition(matrix_one, matrix_two)


#De-dup

def remove_duplicate(array):
    new_array = []
    for item in array:
        if item not in new_array:

            new_array.append(item)
    print(new_array)


#Bonus: Matrix Multiplication

def matrix_multiplication(matrix_one, matrix_two):
    print("Matrix Multiplication")
    matrix_multiplication_list = []
    i = 0
    n = 0
    for index in matrix_one:
        matrix_multiplication_number = []
        n = 0
        for number in index:
            result = 0
            result = int(matrix_one[i][n]) * int(matrix_two[i][n])
            n += 1
            matrix_multiplication_number.append(result)
        i += 1

        matrix_multiplication_list.append(matrix_multiplication_number)
    print(matrix_multiplication_list)

matrix_multiplication(matrix_one, matrix_two)
