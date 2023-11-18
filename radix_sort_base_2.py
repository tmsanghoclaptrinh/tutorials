def counting_sort(arr, exp):
    number_elements_of_array = len(arr)
    output = [0] * number_elements_of_array
    count = [0] * 2

    for i in range(number_elements_of_array):
        index = arr[i] // exp
        count[index % 2] += 1

    for i in range(1, 2):
        count[i] += count[i - 1]

    i = number_elements_of_array - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 2] - 1] = arr[i]
        count[index % 2] -= 1
        i -= 1

    for i in range(number_elements_of_array):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 2


# Example usage:
if __name__ == "__main__":
    binary_array = [101, 110, 10, 111, 100, 11, 1, 0]

    radix_sort(binary_array)
    print("Mảng đã được sắp xếp:", binary_array)
