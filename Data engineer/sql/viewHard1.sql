

select Title from tblEpisode

where Title not in
(select Title from tblEpisode e
join tblEpisodeCompanion ec on
e.EpisodeId = ec.EpisodeId
join tblCompanion c on
ec.CompanionId = c.CompanionId
group by Title
having count(CompanionName) = 1)

and

Title not in
(select Title from tblEpisode e
join tblEpisodeEnemy ee on
e.EpisodeId = ee.EpisodeId
join tblEnemy en on
en.EnemyId = ee.EnemyId
group by Title
having count(EnemyName) = 1)