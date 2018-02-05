from Field import Field
class Category:
   name = ""
   fields = []
   def __init__(self, name, value):
        self.name = name
        self.value = value
   def has_fields(self):
        if len(self.fields) > 0:
            return True
        else:
            return False
   def fill_field(self,field_name,field_value):
        self.fields.append(Field(field_name,field_value))
