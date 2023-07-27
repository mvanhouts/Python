select SUBSTRING(CategoryName, 1, 1) as [Category Initial],
COUNT(EventID) as [Number of events],
AVG(len(EventName)) as [Average event name length]
from tblCategory c
join tblEvent e on
c.CategoryID = e.CategoryID
group by SUBSTRING(CategoryName, 1, 1)