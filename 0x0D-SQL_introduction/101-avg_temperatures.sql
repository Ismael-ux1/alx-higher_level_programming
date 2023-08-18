-- Displays the average temepreture (Fahrenheit) by city orderd by temperature (descending)
SELECT city, AVG(temperature) AS average_temperature
FROM weather_data
GROUP BY city
ORDER BY average_temperature DESC;
