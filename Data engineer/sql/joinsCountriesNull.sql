select CountryName, EventName
from tblCountry
full outer join tblEvent
on tblCountry.CountryID = tblEvent.CountryID
where EventName is null