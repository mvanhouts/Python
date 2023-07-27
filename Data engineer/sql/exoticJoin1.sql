select CompanionName
from tblCompanion c
full outer join tblEpisodeCompanion e
on c.CompanionId = e.CompanionId
where e.CompanionId is null