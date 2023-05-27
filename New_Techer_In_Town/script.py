from roster import student_roster
import classroom_organizer
import itertools
#Creation of the iterator
iterator  = student_roster.__iter__()
#Creationo of the next steps into __next__() method
GoNext = iterator.__next__()

#printing the final list of the combinations
print(classroom_organizer.list_of_combinations)
