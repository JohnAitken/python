-- SQLite
SELECT episodeid, title, first_diffusion, doctorid
FROM `all-detailsepisodes`

where title like ("%romans%");

SELECT * FROM dwguide WHERE title like ("%romans%");

SELECT * FROM 'all-scripts' WHERE episodeid = "2-4";