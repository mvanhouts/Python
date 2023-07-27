select year(EpisodeDate) as [EpisodeYear], EnemyName, count(*) as [Number of episodes]
from tblEpisode
join tblDoctor on
tblEpisode.DoctorId = tblDoctor.DoctorId
join tblEpisodeEnemy on 
tblEpisode.EpisodeId = tblEpisodeEnemy.EpisodeId
join tblEnemy on
tblEpisodeEnemy.EnemyId = tblEnemy.EnemyId
where year(BirthDate) < 1970
group by year(EpisodeDate),EnemyName
having count(*) > 1
order by year(EpisodeDate) asc
