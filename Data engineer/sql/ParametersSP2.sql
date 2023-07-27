--Create a stored procedure to list out the category name, 
--event date and category id for each event

alter procedure sp_CategoryEvents 
@CategoryName varchar(20) = null,
@After date = null,
@CategoryID int = null

as	
begin
begin try
	begin transaction
	select CategoryName, EventDate, c.CategoryID 
	from tblCategory c
	join tblEvent e on
	c.CategoryID = e.CategoryID
	where @CategoryName is null or
	CategoryName like '%' + @CategoryName + '%'
	and @After is null or
	EventDate = @After
	and c.CategoryID is null or
	c.CategoryID = @CategoryID
	group by CategoryName, EventDate ,c.CategoryID
	order by EventDate asc
	commit transaction
end try

begin catch
	raiserror ('Error: ',16, 1)
	rollback transaction
end catch

end

exec sp_CategoryEvents 