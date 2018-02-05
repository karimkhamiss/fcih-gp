from Field import Field
fields = []
field1 = Field("A",20)
field2 = Field("A",0)
fields.append(field1)
fields.append(field2)
field2.fill_constraint("male",">20")
field2.fill_constraint("female","10 - 20")
print(field2.constraints[0].name)