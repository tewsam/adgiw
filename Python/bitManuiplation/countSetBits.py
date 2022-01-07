def countSetBits(num):
	result=0
	while(num > 0):
		if((num & 1) == 1):
			result +=1
		num = num >> 1
	return result

#1101
print(countSetBits(13))