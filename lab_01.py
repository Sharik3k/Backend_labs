array1 = []
array2 = []

with open('input_1.txt', 'r') as file:
    for line in file:
   
        numbers = line.split()
        if len(numbers) == 2:
            array1.append(int(numbers[0]))
            array2.append(int(numbers[1]))

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):  
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_l = selection_sort(array1)
sorted_l2 = selection_sort(array2)

array3 = []
for i in range(len(sorted_l)): 
    minus = sorted_l[i] - sorted_l2[i]
    if minus < 0:
        minus = sorted_l2[i] - sorted_l[i]  
        
    array3.append(minus)


total_sum = sum(array3)


print("висновок", total_sum)