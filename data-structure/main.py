"This would create first object of Constraints class"
from Constraints import Constraint

con1 = Constraints("male", 2000)
"This would create second object of Constraints class"
con2 = Constraints("female", 5000)
print(con2.name)
print ("Total Constraints %d" % Constraints.count)
a