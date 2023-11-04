
# Converting lists of tuples into
# pandas Dataframe.
#List1
Name = ['tomy', 'krish', 'nickol', 'juli']
 
# List2
marks = [75, 80, 56, 62]
list_of_tuples = list(zip(Name, marks))
df = pd.DataFrame(list_of_tuples, columns = ['Name', 'marks'])

  
# Print data.
df

