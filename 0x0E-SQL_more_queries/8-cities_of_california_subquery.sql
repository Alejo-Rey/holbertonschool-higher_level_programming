-- lists all cities with a subquery
SELECT cities.id, name FROM cities
WHERE state_id = (
      SELECT states.id FROM states WHERE name = 'California'
)
ORDER BY cities.id;
