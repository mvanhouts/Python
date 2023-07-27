create function ReignInDays(
@StartDate date,
@EndDate date)
returns int
as
begin
	return datediff(day,@StartDate, @EndDate)
end

select DoctorName, 
dbo.ReignInDays(FirstEpisodeDate, LastEpisodeDate) as [Reign in days]
from tblDoctor
order by [Reign in days] desc