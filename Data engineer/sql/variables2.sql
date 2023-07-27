declare @EventInfo varchar(20) = 'Summary of Events'
declare @EarliestDate date = 
(select min(EventDate) from tblEvent)
declare @LatestDate date = 
(select max(EventDate) from tblEvent)
declare @NumberOfEvents int =
(select count(*) from tblEvent)

select @EventInfo as [Title],
@EarliestDate as [Earliest Date],
@LatestDate as [Latest Date],
@NumberOfEvents as [Number of Events]