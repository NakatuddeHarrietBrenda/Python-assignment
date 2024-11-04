#lists 
#sets 
#tupples 
#diction

#xtics
# -mutable
# -index
# -item

#LISTS 
studentNames = ["Sandra", "Patricia", "Phiona", "Anita"] #strings
marks = [80, 56, 78, 90] #integers
data = ["Sandra", 90, "Kamokya"]

#Access the whole list
print("\nWhole list..\t")
print(studentNames, type(studentNames))

#Accessing list items
#indexes (positive indexes)
print('\n...positive indexes...\t')
print(studentNames[0]) #firt item
print(studentNames[1]) #second item
print(studentNames[2]) #third item

#indexes (negative indexes)
print('\n...negative indexes...\t')
print(studentNames[-3]) #firt item
print(studentNames[-2]) #second item
print(studentNames[-1]) #third item

#Adding new items to the list - Appending
print('\n...append lists...\t')
studentNames.append("Michelle")
print(studentNames)

#insert
print('\n...insert lists...\t')
studentNames.insert(2,"Faith")
print(studentNames)

#Assignment
#Print Patricia,Faith,Phiona and Anita
#Add Masha at the 4th position
#Update the name Phiona to Aladina
#Display the length of the students list
#Print all students names using a for loop
#Calculate the total marks for the students marks variable and the answer is 304

# No. 1
print("\nno. 1\t")

print(studentNames[1])
print(studentNames[2])
print(studentNames[3])
print(studentNames[4])

# No. 2
print("\nno. 2\t")

studentNames.insert(3,"Masha")
print(studentNames)

# No. 3
print("\nno. 3\t")
studentNames.remove("Phiona")
studentNames.insert(4,"Aladina")
print(studentNames)

#Approach 2
studentNames[4] = "Aladina"
print(studentNames)

# No. 4
print("\nno. 4\t")

print(len(studentNames))

# No. 5
print("\nno. 5\t")

for student in studentNames:
    print(student)

# No. 6
print("\nno. 6\t")

totalMarks = sum(marks)

print(f"Total Marks:{totalMarks}")