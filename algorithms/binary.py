

#Binary Search Algorithm:  #Binary Search Algorithm:

search = input("Get search from user!")

min = 0

max = records - 1       #can also use len(listName) for 'records' value


mid = int((min + max) / 2)

#this is for INCREASING order

while (min < max and search != listName[mid]):

   if search < listName[guess]:

       max = guess - 1

   else:

       min = guess + 1

   mid = int((min + max) / 2)

if search == listName[mid]:

    #found them! use 'guess' for index of found search item

else:

    #boooo not found
 