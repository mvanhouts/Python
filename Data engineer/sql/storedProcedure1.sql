alter procedure spMoffats as
begin
begin transaction
	begin try
	select Title from tblEpisode e
	join tblAuthor a on
	a.AuthorId = e.AuthorId
	where AuthorName = 'Steven Moffat'
	commit transaction
	end try

begin catch
	rollback transaction
end catch
end