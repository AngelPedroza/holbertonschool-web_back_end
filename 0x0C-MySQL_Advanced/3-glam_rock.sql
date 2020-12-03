-- If null set the 2020 and get all band with glam style
select band_name, IFNULL(split, 2020) - IFNULL(formed, 0) as lifespan
from metal_bands
where style like '%Glam rock%'
order by 2 DESC;