from flask import Flask, render_template, url_for, request, Response, jsonify
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/actors')
def actor_page():
    top_actors = queries.get_top_10_actors()
    roles = 0
    for character in top_actors:
        roles += character["counts"]
    return render_template('actor.html', top_actors=top_actors, roles=roles)


@app.route('/pa33', methods=["GET"])
def epa3():
    season = request.args.get("season")
    episode = request.args.get("episode")
    if season == "" and episode == "":
        shows = [{"number": "Give input to get result"}]
        return render_template("entry3.html", number=shows)
    else:
        if season == "":
            season = 0
        if episode == "":
            episode = 0
        shows = queries.get_shows_by_search(season, episode)
        return render_template("entry3.html", number=shows)


@app.route('/genres')
def genre_buttons_page():
    genres = queries.get_genres()
    return render_template("genre-buttons.html", genres=genres)


@app.route('/genres/<genre>')
def get_genre_data(genre):
    show_data = queries.get_shows_by_genre(genre)
    return jsonify(show_data)


@app.route('/stars')
def stars():
    genres = queries.list_of_genres()
    return render_template('stars.html', genres=genres)


@app.route('/stars/<genre>')
def get_stars(genre):
    shows = queries.get_shows_with_rating_by_genre(genre)
    return jsonify(shows)


@app.route('/ranger')
def ranger():
    shows = queries.get_shows_with_season()
    numbers = []
    for show in shows:
        numbers.append(show["count"])
    return render_template('ranger.html', shows=shows, max=max(numbers))


@app.route('/pa11')
def pa11_1():
    genres = queries.shows_pa11_genre()
    return render_template('pa11.html', genres=genres)


@app.route('/pa11/<genre>')
def pa11_2(genre):
    shows = queries.shows_pa11(genre)
    return jsonify(shows)


@app.route('/pa3')
def pa3():
    datas = {}
    shows = queries.shows_pa3_total_runtime()
    for show in shows:
        name_list = []
        title = show['title']
        names = queries.shows_pa3_actors(show["title"])
        for name in names:
            name_list.append(name["name"])
        datas[title] = name_list
    return render_template('pa3.html', shows=shows, datas=datas)


@app.route('/pa2')
def pa2():
    data = queries.get_pa2()
    return render_template('pa2.html', datas=data)


@app.route('/pa8')
def pa8():
    year = 2010
    datas = queries.get_pa8(str(year))
    for data in datas:
        if data["age_then"] is not None:
            if data["age_then"] > data["show_age"]:
                data["was_older"] = True
            else:
                data["was_older"] = False
        else:
            data["was_older"] = "unknown"

    return render_template('pa8.html', datas=datas, year=year)


@app.route('/pa5')
def p5():
    actors = queries.get_pa5()
    return render_template('pa5.html', actors=actors)


@app.route('/pa4')
def p4_1():
    return render_template('pa4.html')


@app.route('/pa4/<search>')
def p4_2(search):
    shows = queries.get_pa4(search)
    return jsonify(shows)


@app.route('/pa6')
def p6():
    year_input = request.args.get("date")
    year = f"{year_input}-01-01"
    actors = queries.get_pa6(year)
    return render_template('pa6.html', actors=actors)


@app.route('/pa7')
def p7():
    genre = request.args.get("genre")
    shows = queries.get_pa7_1(genre)
    genres = queries.get_pa7_2()
    return render_template('pa7.html', shows=shows, genres=genres)


@app.route('/pa9')
def pa9():
    return render_template('pa9.html')


@app.route('/pa9/<phrase>')
def pa9_1(phrase):
    searched_phrase = f"%{phrase}%"
    characters = queries.get_pa9(searched_phrase)
    return jsonify(characters)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
