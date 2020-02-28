import datetime
d = datetime.date(2020, 2, 22)
 
print( d.day, d.month, d.year)
 # yesterday

import datetime
d = datetime.date(2020, 2, 23)
 
print( d.day, d.month, d.year)

#today

import datetime
d = datetime.date(2020, 1, 23)
 
print( d.day, d.month, d.year)

#1 mouth ago 

from datetime import datetime
deadline = datetime.strptime("01/01/2017 12:10:03.234567", "%d/%m/%Y%H%M%S.%P")
print(deadline)  