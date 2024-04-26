SELECT
    Weather.id
FROM
    Weather
JOIN
    Weather oth
ON
    Weather.recordDate - 1 = oth.recordDate 
WHERE
    Weather.temperature > oth.temperature;