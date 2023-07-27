select AuthorName, DoctorName, count(EpisodeNumber) as Episodes
from tblAuthor
inner join tblEpisode
on tblAuthor.AuthorId = tblEpisode.AuthorId
inner join tblDoctor
on tblEpisode.DoctorId = tblDoctor.DoctorId
group by AuthorName, DoctorName
having count(EpisodeNumber) > 5