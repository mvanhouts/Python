create procedure spSummariseEpisodes
as
begin
begin try
	begin transaction
	select top 3 CompanionName, count(Title) 
	from tblCompanion c
	join tblEpisodeCompanion ec on
	c.CompanionId = ec.CompanionId
	join tblEpisode e on
	ec.EpisodeId = e.EpisodeId
	group by CompanionName
	order by count(Title) desc

	select top 3 EnemyName, count(Title) 
	from tblEnemy e
	join tblEpisodeEnemy ee
	on e.EnemyId = ee.EnemyId
	join tblEpisode ed
	on ee.EpisodeId = ed.EpisodeId
	group by EnemyName
	order by count(Title) desc
	commit transaction
end try

begin catch
	rollback transaction
end catch
end
