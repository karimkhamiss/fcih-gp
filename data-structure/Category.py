from Field import Field
class Category:
   name = ""
   fields = []
   def __init__(self, name):
        self.name = name
   def has_fields(self):
        if len(self.fields) > 0:
            return True
        else:
            return False
   def fill_fields(self,field_name,field_value):
        self.fields.append(Field(field_name,field_value))
