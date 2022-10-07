from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_top_10_actors():
    return data_manager.execute_select('''SELECT 
    a.name,
    COUNT(sc.character_name) AS counts
    FROM actors a
    JOIN show_characters sc ON a.id = sc.actor_id
    GROUP BY a.name
    ORDER BY counts DESC 
    LIMIT 10
    ;''')


def get_shows_by_search(season, episode):
    return data_manager.execute_select('''SELECT 
    COUNT(distinct (show_id)) AS number
    FROM seasons s
    JOIN episodes ep ON s.id = ep.season_id
    WHERE season_number > %(season)s AND ep.episode_number > %(episode)s
    ;''', {"season": season, "episode": episode})


def get_total_shows_by_genre():
    return data_manager.execute_select('''
    SELECT sh.title, g.name
    FROM shows sh
    JOIN show_genres sg on sh.id = sg.show_id
    JOIN genres g on g.id = sg.genre_id
    GROUP BY sh.title, g.name
    ;''')


def get_shows_by_genre(genre):
    return data_manager.execute_select('''SELECT 
        sh.title,
        g.name,
        EXTRACT(YEAR FROM sh.year) AS year
        FROM shows sh
        LEFT JOIN show_genres sg ON sh.id = sg.show_id
        LEFT JOIN genres g ON sg.genre_id = g.id
        WHERE g.name = %(genre)s
        ;''', {"genre": genre})


def get_genres():
    return data_manager.execute_select('''SELECT 
            DISTINCT(name)
            FROM genres
            JOIN show_genres sg ON genres.id = sg.genre_id
            ;''')


def get_shows_with_rating_by_genre(genre):
    return data_manager.execute_select('''SELECT 
    DISTINCT(s.id), 
    s.title,
    EXTRACT(year from s.year) AS year,
    ROUND(s.rating, 1) as rating
    FROM shows s
    JOIN show_genres sg ON s.id = sg.show_id
    JOIN genres g ON sg.genre_id = g.id
    WHERE g.name = %(genre)s
    ORDER BY rating DESC
    LIMIT 10
    ;''', {"genre": genre})


def list_of_genres():
    return data_manager.execute_select('''SELECT 
    name as genres
    FROM genres
    ;''')


def get_shows_with_season():
    return data_manager.execute_select('''SELECT 
    sh.title,
    COUNT(sh.title) AS count
    FROM shows sh
    JOIN seasons s ON sh.id = s.show_id
    GROUP BY sh.id, sh.title
    ORDER BY count
    ;''')


def shows_pa11(genre):
    return data_manager.execute_select('''SELECT 
        sh.title,
        g.name AS genre,
        COUNT(e.id) AS episodes
        FROM shows sh
        JOIN show_genres sg ON sh.id = sg.show_id
        JOIN genres g ON sg.genre_id = g.id
        JOIN seasons s ON sh.id = s.show_id
        JOIN episodes e ON s.id = e.season_id
        WHERE g.name = %(genre)s
        GROUP BY sh.title, g.name
        HAVING COUNT(e.id) > 20
        ORDER BY episodes DESC
        LIMIT 50
        ;''', {"genre": genre})


def shows_pa11_genre():
    return data_manager.execute_select('''SELECT
    name
    FROM genres 
    ;''')


def shows_pa3_total_runtime():
    return data_manager.execute_select('''SELECT
    sh.title
    FROM shows sh
    JOIN seasons s ON sh.id = s.show_id
    JOIN episodes e ON s.id = e.season_id
    GROUP BY sh.title, sh.runtime
    ORDER BY COUNT(e.id) * sh.runtime DESC
    LIMIT 10
    ;''')


def shows_pa3_actors(title):
    return data_manager.execute_select('''SELECT
    a.name
    FROM actors a
    JOIN show_characters sc ON a.id = sc.actor_id
    JOIN shows sh ON sc.show_id = sh.id
    WHERE sh.title = %(title)s
    ;''', {"title": title})


def get_pa2():
    return data_manager.execute_select('''SELECT
     EXTRACT(year FROM (sh.year))::INTEGER AS year,
     ROUND(AVG(sh.rating), 1) AS rating,
     COUNT(sh.id) AS shows
     FROM shows sh
     WHERE year >= '1970/01/01' AND year < '2011/01/01'
     GROUP BY year
     ORDER BY year
     ;''')


def get_pa8(age):
    return data_manager.execute_select('''SELECT
     a.name,
     EXTRACT(year from AGE(a.birthday))::integer as age,
     EXTRACT(year from AGE(sh.year))::integer as show_age,
     EXTRACT(year from AGE(a.birthday))::integer - EXTRACT(year from AGE(sh.year))::integer as age_then
     FROM shows sh
     JOIN show_characters sc ON sh.id = sc.show_id
     JOIN actors a ON sc.actor_id = a.id
     WHERE EXTRACT(year FROM sh.year) = '1995'
     ORDER BY age DESC 
     ;''')

# , {"age": age})
# return data_manager.execute_select("SELECT %s  FROM shows sh", (AsIs(column),))


def get_pa5():
    return data_manager.execute_select('''SELECT
    a.name,
    EXTRACT(year from AGE(a.birthday))::integer as age,
    COUNT(sh.id) as count,
    a.death
    FROM shows sh
    JOIN show_characters sc ON sh.id = sc.show_id
    JOIN actors a ON sc.actor_id = a.id
    WHERE EXTRACT(year from AGE(a.birthday)) IS NOT NULL
    GROUP BY a.name, age, a.death
    ORDER BY count DESC
    LIMIT 80
     ;''')


def get_pa4(phrase):
    title = f"%{phrase}%"
    return data_manager.execute_select('''SELECT
    title,
    ROUND(rating, 1) as rating,
    to_char(year,'yyyy/mm/dd/D') as year,
    trailer
    FROM shows 
    WHERE title ILIKE %(title)s
    ;''', {"title": title})


def get_pa6(year):
    return data_manager.execute_select('''SELECT 
    a.name,
    to_char(a.birthday, 'YYYY-MM-DD' ) AS birthday,
    COUNT(sc.character_name) AS characters,
    ROUND(AVG(sh.rating), 1) AS rating
    FROM show_characters sc
    JOIN shows sh ON sc.show_id = sh.id 
    JOIN actors a ON sc.actor_id = a.id 
    WHERE to_char(a.birthday, 'YYYY-MM-DD' ) IS NOT NULL AND to_char(a.birthday, 'YYYY-MM-DD' ) > %(year)s
    GROUP BY a.name, a.birthday
    ;''', {'year': year})


def get_pa7_1(genre):
    return data_manager.execute_select('''SELECT 
    sh.title,
    COUNT(sc.id) AS character_count
    FROM show_genres sg
    JOIN shows sh ON sg.show_id = sh.id
    JOIN genres g ON sg.genre_id = g.id
    JOIN show_characters sc ON sh.id = sc.show_id
    WHERE g.name = %(genre)s
    GROUP BY sh.title
    ;''', {"genre": genre})


def get_pa7_2():
    return data_manager.execute_select('''SELECT 
    g.name
    FROM show_genres sg
    JOIN shows sh ON sg.show_id = sh.id
    JOIN genres g ON sg.genre_id = g.id
    GROUP BY g.name
    ;''')


def get_pa9(phrase):
    return data_manager.execute_select('''SELECT 
    sc.character_name AS character,
    a.name,
    sh.title
    FROM show_characters sc
    JOIN actors a ON sc.actor_id = a.id
    JOIN shows sh ON sc.show_id = sh.id
    WHERE sc.character_name ILIKE %(phrase)s
    GROUP BY character, a.name, sh.title
    ;''', {"phrase": phrase})
