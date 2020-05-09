from flask import Flask, render_template, url_for, request
#from flask_googlemaps import GoogleMaps
import sqlite3


#from facebook_scrapper import get_posts
app = Flask(__name__)
#app.config['GOOGLEMAPS_KEY'] = 'AIzaSyA4AkTJLdwf4DKt9DjEH4J2iQXv1E_emjU'
#GoogleMaps(app)
#facebook_posts = []
#conn = sqlite3.connect('hawkerhelp.db') 
#c = conn.cursor()

#for post in get_posts(group = '268960887438286', pages = 1):
#    facebook_posts.append(post)

# shows page about what HawkerHelp is
@app.route("/") 
def index():
    return render_template("index.html")

# actual main page with search and everything
@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/search')
def search():
    search = request.args.get('search')
    conn = sqlite3.connect('hawkerhelp.db') 
    c = conn.cursor()
    results = c.execute("SELECT * FROM Hawkers WHERE Stallname LIKE '%" + search + "%' OR StallType LIKE '%"+ search + "%';").fetchall()
    #print(results)
    #print(rows)
    return render_template('search.html',results = results)


@app.route('/sataymankim')
def hawker1():
    return render_template("hawker1.html")


'''@app.route('/', methods =['POST', 'GET']) #get location
def result():
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
    if request.method == 'POST':
        location = request.form["location"]
        location = location.strip()
        if (location != ''):
            location_detail = {'address':location}
            r = request.get(url = URL, params = location_detail)
            data = r.json()
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            formatted_address =  data['results'][0]['formatted_address']
        else:
            latitude = "No input given"
            longitude = "No input given"
            formatted_address = "No input given"

    if latitude == "No input given":
        mymap = Map(
            identifier="view-side",
            lat=latitude,
            lng=longitude,
            markers=[(latitude, longitude)]
        )
    else:
        pass
    return render_template(test.html, mymap=mymap)'''


if __name__ == "__main__":
    app.run(debug = True)