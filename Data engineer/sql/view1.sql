alter view EventsByCategory as
select CategoryName, count(*) as [NumberEvents]
from tblCategory c
join tblEvent e
on c.CategoryID = e.CategoryID
group by CategoryName

select * from EventsByCategory
where NumberEvents > 50