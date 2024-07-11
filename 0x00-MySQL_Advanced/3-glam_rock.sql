-- List bands with Glam rock as style ranked by their longevity
-- sql scripts that does that
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
