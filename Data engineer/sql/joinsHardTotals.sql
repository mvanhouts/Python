select AuthorName,Title,DoctorName, EnemyName, 
	(
	select (len(AuthorName) + len(Title) + len(DoctorName) + len(EnemyName))
	) as [TotalLength]
from tblAuthor
inner join tblEpisode
on tblAuthor.AuthorId = tblEpisode.AuthorId
inner join tblDoctor
on tblEpisode.DoctorId = tblDoctor.DoctorId
inner join tblEpisodeEnemy
on tblEpisode.EpisodeId = tblEpisodeEnemy.EpisodeId
inner join tblEnemy
on tblEpisodeEnemy.EnemyId = tblEnemy.EnemyId
where (
	select (len(AuthorName) + len(Title) + len(DoctorName) + len(EnemyName))
	) < 41