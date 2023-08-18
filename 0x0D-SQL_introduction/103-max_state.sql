-- Displays the maximum temperature of each state, ordered by state name
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `tempratures`
GROUP BY `state`
ORDER BY `state`;
