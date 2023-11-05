#List1
Name = ['tomy', 'krish', 'nickol', 'juli']
 
# List2
marks = [75, 80, 56, 62]

#Above two lists can be merged by using list(zip()).
tuples = list(zip(Name, marks))

result = [item for t in tuples for item in t]
print("Convert list of tuples into list: ",result)
