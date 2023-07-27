select concat((year(EventDate) / 100) + 1,'th century') as century,
count(*) as [Number of events]
from tblEvent
group by concat((year(EventDate) / 100) + 1,'th century')