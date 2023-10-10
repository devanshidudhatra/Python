# # # # # Python program for implementation of Bubble Sort

# # # # def bubbleSort(arr):
# # # # 	n = len(arr)
# # # # 	# optimize code, so if the array is already sorted, it doesn't need
# # # # 	# to go through the entire process
# # # # 	swapped = False
# # # # 	# Traverse through all array elements
# # # # 	for i in range(n-1):
# # # # 		# range(n) also work but outer loop will
# # # # 		# repeat one time more than needed.
# # # # 		# Last i elements are already in place
# # # # 		for j in range(0, n-i-1):

# # # # 			# traverse the array from 0 to n-i-1
# # # # 			# Swap if the element found is greater
# # # # 			# than the next element
# # # # 			if arr[j] > arr[j + 1]:
# # # # 				swapped = True
# # # # 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
# # # # 		if not swapped:
# # # # 			# if we haven't needed to make a single swap, we
# # # # 			# can just exit the main loop.
# # # # 			return


# # # # # Driver code to test above
# # # # arr = [64, 34, 25, 12, 22, 11, 90]

# # # # bubbleSort(arr)

# # # # print("Sorted array is:")
# # # # for i in range(len(arr)):
# # # # 	print("% d" % arr[i], end=" ")
# # # # Python program for implementation of Selection
# # # # Sort

# # # A = [64, 25, 12, 22, 11]

# # # # Traverse through all array elements
# # # for i in range(len(A)):
	
# # # 	# Find the minimum element in remaining
# # # 	# unsorted array
# # # 	min_idx = i
# # # 	for j in range(i+1, len(A)):
# # # 		if A[min_idx] > A[j]:
# # # 			min_idx = j
			
# # # 	# Swap the found minimum element with
# # # 	# the first element	
# # # 	A[i], A[min_idx] = A[min_idx], A[i]

# # # # Driver code to test above
# # # print ("Sorted array")
# # # for i in range(len(A)):
# # # 	print("%d" %A[i],end="  ")

# # # Python 3 program for recursive binary search.
# # # Modifications needed for the older Python 2 are found in comments.

# # # Returns index of x in arr if present, else -1
# # def binary_search(arr, low, high, x):

# # 	# Check base case
# # 	if high >= low:

# # 		mid = (high + low) // 2

# # 		# If element is present at the middle itself
# # 		if arr[mid] == x:
# # 			return mid

# # 		# If element is smaller than mid, then it can only
# # 		# be present in left subarray
# # 		elif arr[mid] > x:
# # 			return binary_search(arr, low, mid - 1, x)

# # 		# Else the element can only be present in right subarray
# # 		else:
# # 			return binary_search(arr, mid + 1, high, x)

# # 	else:
# # 		# Element is not present in the array
# # 		return -1

# # # Test array
# # arr = [ 2, 3, 4, 10, 40 ]
# # x = 10

# # # Function call
# # result = binary_search(arr, 0, len(arr)-1, x)

# # if result != -1:
# # 	print("Element is present at index", str(result))
# # else:
# # 	print("Element is not present in array")
# # Python code for finding union and intersection of linkedList


# class linkedList:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None

# 	def insert(self, data):
# 		if self.head is None:
# 			self.head = Node(data)
# 			self.tail = self.head
# 		else:
# 			self.tail.next = Node(data)
# 			self.tail = self.tail.next


# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

# # return the head of new list containing the intersection of 2 linkedList


# def findIntersection(head1, head2):
# 	# creating a map
# 	hashmap = {}

# 	# traversing on first list
# 	while(head1 != None):
# 		data = head1.data
# 		if(data not in hashmap.keys()):
# 			hashmap[data] = 1
# 		head1 = head1.next

# 	# making a new linkedList
# 	ans = linkedList()
# 	while(head2 != None):
# 		data = head2.data
# 		if(data in hashmap.keys()):
# 			# adding data to new list
# 			ans.insert(data)
# 		head2 = head2.next
# 	return ans.head

# # return the head of new list containing the union of 2 linkedList


# def union(head1, head2):
# 	# creating a map
# 	hashmap = {}

# 	# traversing on first list
# 	while(head1 != None):
# 		data = head1.data
# 		if(data not in hashmap.keys()):
# 			hashmap[data] = 1
# 		head1 = head1.next

# 	while(head2 != None):
# 		data = head2.data
# 		if(data not in hashmap.keys()):
# 			hashmap[data] = 1
# 		head2 = head2.next

# 	# making a new linkedList
# 	ans = linkedList()

# 	# traverse on hashmap
# 	for key, value in hashmap.items():
# 		ans.insert(key)

# 	return ans.head


# def printList(head):
# 	while head:
# 		print(head.data, end=' ')
# 		head = head.next
# 	print()


# if __name__ == '__main__':

# 	# first list
# 	ll1 = linkedList()
# 	ll1.insert(1)
# 	ll1.insert(2)
# 	ll1.insert(3)
# 	ll1.insert(4)
# 	ll1.insert(5)

# 	# second list
# 	ll2 = linkedList()
# 	ll2.insert(1)
# 	ll2.insert(3)
# 	ll2.insert(5)
# 	ll2.insert(6)

# 	print("First list is ")
# 	printList(ll1.head)

# 	print("Second list is ")
# 	printList(ll2.head)

# 	print("Intersection list is")
# 	printList(findIntersection(ll1.head, ll2.head))

# 	print("Union list is ")
# 	printList(union(ll1.head, ll2.head))


# # This code is contributed by Arpit Jain
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
