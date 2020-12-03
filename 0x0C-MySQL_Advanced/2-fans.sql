-- Get the total fans by country
select origin, sum(fans) as nb_fans
from metal_bands
group by 1
order by 2
DESC;