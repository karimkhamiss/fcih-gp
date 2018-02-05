from Constraint import Constraint
class Field:
   name = ""
   value = ""
   counter = 0
   constraints = []
   def __init__(self, name, value):
        Field.counter+=1
        self.name = name
        self.value = value
   def has_constraints(self):
        if len(self.constraints) > 0:
            return True
        else:
            return False
   def fill_constraint(self,constraint_name,constraint_value):
        self.constraints.append(Constraint(constraint_name,constraint_value))
   def fields_count(self):
        return Field.counter
