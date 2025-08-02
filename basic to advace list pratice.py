'''#1.Find the maximum and minimum element in a list
n = input("enter the len of the list:")
my_list = list(map(int,input("enter the element of the list:").split()))
print(max(my_list),min(my_list))

#2.Reverse a list without using reverse()
n = int(input("enter the no of elements:"))
mylist =[]
for i in range(n):
  num = int(input(f"enter the no {i+1}:"))
  mylist.append(num)
print("reversed list",mylist[::-1])

#3.Remove duplicates from a list
list = [2,3,4,5,3,4,5,7,8]
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)        

#4.Count the frequency of each element
l1 = [2,3,4,5,6,7,4,4,3,3,2,7,7]
l1.sort()
for i in set(l1):
    count = l1.count(i)
    print(f"freq of {i}:{count}")'''

#5.Find the second largest element in a list
l = [2,3,4,5,6,7,7,2,4,9,9]
l2 = list(set(l))
l2.sort()
print(l2[-2])

#6.Check if the list is sorted (ascending or descending)
l = [1,2,34,6,89,56]
sorted_list = sorted(l)
is_aces = True
for i in range(len(sorted_list)-1):
    if sorted_list[i] < sorted_list[i+1]:
        break
if is_aces is True:
    print("ascending")
else:
    print("descending")    
        
#7.Merge two sorted lists into a single sorted list
l1 =[2,3,4,7]
l2 = [2,8,6] 
l3 = l1 + l2
print(l3)      
    
#8.Find the sum and average of list elements
l = [1.5,7,56,45,32,0]
print("sum:",sum(l))
print("length:",len(l))    

#9.Find all even and odd numbers in a list
l = [1,2,3,4,6,7,4]
even_list = []
odd_list = []
for i in l:
    if i%2 == 0:
        even_list.append(i)
    else:
       odd_list.append(i) 
print("list of even numbers:",even_list)       
print("list of odd no:", odd_list)    

#10.Print elements at even and odd indices
l = [2,6,8,9,10,5,34,23,11]
print("no at even indices",l[::2])
print("no at odd indices",l[1::2])
