select e.EventName, e.EventDetails
from tblEvent e

where 

e.CountryID not in
(select top 30 c.CountryID from tblCountry c
order by CountryName desc)

and 

e.CategoryID not in
(select top 15 CategoryID from tblCategory
order by CategoryName desc)

order by e.EventDate
