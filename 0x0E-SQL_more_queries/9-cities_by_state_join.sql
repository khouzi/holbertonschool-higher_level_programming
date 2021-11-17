-- lists all cities contained in the database hbtn_0d_usa.
FROM states, cities SELECT cities.id, cities.name, states.name ORDER BY cities.id ASC;