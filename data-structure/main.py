from Category import Category
categorys = []
category1 = Category("A",20)
category2 = Category("A",0)
categorys.append(category1)
categorys.append(category2)
category2.fill_field("male",">20")
category2.fill_field("female","10 - 20")
category2.fields[0].fill_constraints("adult",">20")
print(category2.fields[0].constraints[0].name)