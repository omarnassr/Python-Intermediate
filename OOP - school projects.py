class School():
  #main proprities of class - construction method.
  def __init__(self, name, level, numberOfStudents):
    self.name = str(name)
    self.level = str(level)
    self.numberOfStudents = int(numberOfStudents)
  # All properties have gethers.
  def getName(self):
      return  self.name
  def getLevel(self):
      return self.level
  def getNumberOfStudents(self):
      return self.numberOfStudents
  # Only setNumber have setter!
  def setNumberOfStudents(self, new):
      self.numberOfStudents = new
  # Display the information about class.
  def __repr__(self):
      return str("A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents))

#child classes
#1
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'Primary School', numberOfStudents )
    self.pickupPolicy = str(pickupPolicy)

  def getPickupPolicy(self):
    return self.pickupPolicy

  def setPickupPolicy(self, newPolicy):
    self.pickupPolicy = newPolicy

    def __repr(self):
      return super().__repr__() + "The pickup Policy is {}".format(self.pickupPolicy)
#2
class MiddleSchool(School):
  pass
#3
class HighSchool(School):
  def __init__(self, name,  numberOfStudents, sportsTeams):
    super().__init__(name, 'High School', numberOfStudents )
    self.sportsTeams = list()

    def getSportsTeams(self):
      return self.sportsTeams

    def __repr__(self):
      return super().__repr__() + "Our sports Teams are as listed {}".format(self.sportsTeams)


# Instantiations.

School_No1 = School("Jacksonville Beach Elementary School", "primary", 1000)

psc = PrimarySchool('Kacksonlela Tree Elementry School', 500, " ALL VISITORS MUST SIGN IN AT THE MAIN OFFICE; PHOTO ID IS REQUIRED." )
print(psc)

hsc = HighSchool('7okshasville Na5la Elementry School', 280, ["7oka1", "7oka2", "Mido101"] )

