-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT sht.title, shg.genre_id FROM tv_shows AS sht
JOIN tv_shows_genres AS shg ON sht.id = shg.show_id
ORDER BY sht.title, shg.genre_itd;