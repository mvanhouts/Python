alter procedure sp_SearchEnemy 
@Enemy as varchar(20)
as

begin
begin transaction
	begin try
	select SeriesNumber, EpisodeNumber, Title
	from tblEpisode e
	join tblEpisodeEnemy ee on
	e.EpisodeId = ee.EpisodeId
	join tblEnemy ey on
	ee.EnemyId = ey.EnemyId
	where EnemyName like '%' + @Enemy + '%'
	commit transaction
	end try

begin catch
	RAISERROR ('Error, ',16,1)
	rollback transaction
end catch
end

exec sp_SearchEnemy silence