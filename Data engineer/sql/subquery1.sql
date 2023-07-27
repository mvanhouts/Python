select ContinentName, count(*) as [EventNumber]
from tblContinent ct
join tblCountry cy on
ct.ContinentID = cy.ContinentID
join tblEvent et on
cy.CountryID = et.CountryID
where ct.ContinentName in
	(select top 3 ContinentName
	from tblContinent ct
	join tblCountry cy on
	ct.ContinentID = cy.ContinentID
	join tblEvent et on
	cy.CountryID = et.CountryID
	group by ContinentName
	order by count(*))
group by ContinentName
