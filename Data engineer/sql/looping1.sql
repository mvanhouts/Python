declare @Counter int = 1991
declare @EndValue int = year(getdate())
while @Counter < @EndValue
begin
	declare @NumberEvents int = 
	(select count(*)
	from tblEvent
	where year(EventDate) = @Counter)
	print ('There were '+ cast(@NumberEvents as varchar(20)) + ' events in '+ cast(@Counter as varchar(20)))
	set @Counter = @Counter + 1
end