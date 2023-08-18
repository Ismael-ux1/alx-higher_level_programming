-- Displays the maximum temperature of each state, ordered by state name
SELECT state, MAX(temperature) AS max_temperature
FROM weather_data
GROUP BY state
ORDER BY state;
