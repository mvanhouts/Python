select AuthorName,EpisodeNumber
from tblAuthor
inner join tblEpisode
on tblAuthor.AuthorId = tblEpisode.AuthorId
inner join tblEpisodeEnemy
on tblEpisode.EpisodeId = tblEpisodeEnemy.EpisodeId
inner join tblEnemy
on tblEpisodeEnemy.EnemyId = tblEnemy.EnemyId
where EnemyName = 'Daleks'