select EventName, EventDate, CategoryName
from tblEvent
full outer join
tblCategory on tblEvent.CategoryID = tblCategory.CategoryID
where Eventname is null