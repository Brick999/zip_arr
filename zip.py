def zip_arr(arr1, arr2):
	count = 0
	new_arr = []
	for i in range (0, len(arr1)):
		new_arr.append(arr1[i])
	for j in range (0, len(arr2)):
		new_arr.append(arr2[j])
		k = len(arr1) + count
		while k > 2*count+1:
			(new_arr[k-1], new_arr[k]) = (new_arr[k], new_arr[k-1])
			k = k - 1
		count = count + 1
	return new_arr
arr_1 = [1, 3, 9, 10, 109, 16]
arr_2 = [18,'a', 'b', 'c', 'd', 'e', 'f', 'g']
print zip_arr(arr_1, arr_2)