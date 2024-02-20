-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT sht.title , shg.genre_id
FROM tv_shows AS sht
LEFT JOIN tv_show_genres AS shg
    ON sht.id = shg.show_id
WHERE shg.genre_id IS NULL
ORDER BY sht.title, shg.genre_id;