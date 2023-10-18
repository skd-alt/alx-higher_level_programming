-- lists all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
	LEFT JOIN (
		SELECT tv_shows.title, tv_shows.id
		FROM tv_show_genres
		JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
		JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
		WHERE tv_genres.name = "Comedy"
	) comedy_shows ON comedy_shows.id = tv_shows.id
WHERE comedy_shows.title IS NULL
ORDER BY tv_shows.title;
