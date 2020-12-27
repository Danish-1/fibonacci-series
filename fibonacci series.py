n1=0 #first value
n2 =1 #second value
a = [] #list to store nth term series
n = int(input('enter a number of terms:'))
# give number of terms 
print('fibonacci series:')
if (n<1):
	# condition for Invalid input
	print('enter positive integer value')
else:
	# condition except Invalid input
	for i in range(0,n):
		#print 0 to n terms
		a.append(n1)        # append terms in list
		# logic for series
		nth = n1 + n2
		n1 = n2
		n2 = nth
# print list which contains nth term series
print(a)
print('program ended')
	