arr = [53, 83, 73]

def array_value_index(array, value):
    for i in array:
        if i == value:
            return array.index(value)

def find_max(array):
    return max(array)

max_value = find_max(arr)
print("The max value is: ", max_value)

value_index = array_value_index(arr, max_value)
print("The index of the max value is: ", value_index)