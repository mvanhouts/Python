select AuthorName, Title, EpisodeType 
from tblAuthor
join tblEpisode on 
tblAuthor.AuthorId = tblEpisode.AuthorId
where EpisodeType like '%special%'