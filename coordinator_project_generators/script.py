guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    received_value = yield name 
    if received_value is not None:
      name, age = received_value.split(",")
      guests[name] =  int(age)

def table1(name, table):
      yield (name, "Table1", "Chicken", "Seat No{}".format(table))
    
def table2(name, table):
      yield (name, "Table2", "Beef", "Seat No{}".format(table))
    
def table3(name, table):
      yield (name, "Table3", "Fish", "Seat No{}".format(table))

def assignment(guests):
    counter = 1
    for guest in guests:
      if counter < 6:
        yield from table1(guest, counter)
        counter += 1
      elif counter < 11:
        yield from table2(guest, counter)
        counter+=1
      elif counter < 16:
        yield from table3(guest, counter)
      else:
        print("No more seats available!")
#calling the generator
generator_object = read_guestlist('guest_list.txt')
#looping over 
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
generator_object.send("jane,36")
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)


#generator expression
filter21 = (name for name in guests if guests[name] >= 21)
for ok in filter21:
  print(ok)
print("00000000000000000!000000000000000")
#meals

assignn = assignment(guests)
for i in assignn:
  print(i)
