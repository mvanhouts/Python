alter procedure sp_FirstEvent as

select top 1 ContinentName 
from tblContinent c
join tblCountry cy
on c.ContinentID = cy.ContinentID
join tblEvent e on
cy.CountryID = e.CountryID
order by EventDate asc


create procedure sp_FilteredEvent
declare @ContinentName varchar(50) = 
exec sp_FirstEvent

select EventName, EventDate, ContinentName 
from tblContinent c
join tblCountry cy
on c.ContinentID = cy.ContinentID
join tblEvent e on
cy.CountryID = e.CountryID
