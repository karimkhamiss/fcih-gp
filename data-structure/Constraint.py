class Constraint:
   name = ""
   value = ""
   counter = 0
   def __init__(self, name, value):
        Constraint.counter+=1
        self.name = name
        self.value = value
   def count(self):
        return Constraint.counter
