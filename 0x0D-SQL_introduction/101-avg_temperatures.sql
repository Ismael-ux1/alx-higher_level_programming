-- Displays the average temepreture (Fahrenheit) by city orderd
-- by temperature (descending).
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
