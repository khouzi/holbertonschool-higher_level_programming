-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT name FROM cities WHERE states.name = "California" GROUP BY cities.id DESC;