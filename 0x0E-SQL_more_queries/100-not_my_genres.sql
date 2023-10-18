-- list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
	LEFT JOIN (
		SELECT tv_genres.id AS id, tv_genres.name AS name
		FROM tv_show_genres
		JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
		JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
		WHERE tv_shows.title = "Dexter"
	) dex_genres ON dex_genres.id = tv_genres.id
WHERE dex_genres.id IS NULL
ORDER BY tv_genres.name;
