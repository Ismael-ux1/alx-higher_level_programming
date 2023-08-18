-- Displays the top 3 cities with the highest average temperature during July and August,
-- ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avge_temp`
FROM `temperatures`
WHERE `MONTH` = 7, OR `MONTH` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
