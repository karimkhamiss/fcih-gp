from Category import Category
category_list = []
category1 = Category("Category #1")
category2 = Category("Category #2")
category2.fill_fields("Field #1", " 10 - 20 ")
category2.fill_fields("Field #2", " 10 - 20 ")
category_list.append(category1)
category2.fields[0].fill_constraints("Constraint #1"," > 20 ")
category2.fields[0].fill_constraints("Constraint #2"," < 20 ")
category_list.append(category2)