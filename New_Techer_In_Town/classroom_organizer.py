from roster import student_roster
import itertools

# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
    self.index = 0

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def __iter__(self):
      return self

  def __next__(self):
      if self.index < len(self.sorted_names):
        called = self.sorted_names[self.index]
        self.index += 1
        return called
      else:
        raise StopIteration



  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

student_test = ClassroomOrganizer()
chainer = itertools.chain(student_test.get_students_with_subject('Math'),student_test.get_students_with_subject('Science') )
combiner = itertools.combinations(chainer, 4)

for studentMatch in combiner:
  print(studentMatch)

list_of_combinations = list(combiner)

