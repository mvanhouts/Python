declare @EpisodeId int = 15
declare @EnemyList varchar(100) = ''

select @EnemyList = @EnemyList + 
(select EnemyName from tblEnemy e
join tblEpisodeEnemy ee
on e.EnemyId = ee.EnemyId
join tblEpisode ep
on ee.EpisodeId = ep.EpisodeId
where ep.EpisodeId = @EpisodeId
)