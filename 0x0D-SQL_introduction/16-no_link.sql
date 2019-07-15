-- list all the score checking null and empty values
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name > ""
ORDER BY score DESC;
