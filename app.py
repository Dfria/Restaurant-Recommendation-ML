import os
from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
db = MySQL()
db.init_app(app)
app.debug = True

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_DB'] = 'rrmm'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Yelp API endpoint
YELP_API_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

# Yelp API key (replace with your own)
YELP_API_KEY = 'AEA4hhBn4PY-YMAY4vhVBZmLiip5YlAn4Ban_CjW1JmOPlf0NyzKyEtpOGxJe3L5aECSZZg4_Pxih1zmnBumkS3SiP2zCuS49A6kItATJKbhN395L3qXIGZe7FQbZHYx'


@app.route('/restaurants', methods=['GET', 'POST'])
def get_restaurants():
    if request.method == 'POST':
        location = request.form.get('location')
        
        headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
        params = {'location': location, 'categories': 'restaurants'}
        response = requests.get(YELP_API_ENDPOINT, headers=headers, params=params)
        
        return jsonify(response.json()['businesses'])
    
    elif request.method == 'GET':
        return '''
            <form method="POST">
                <label for="location">Enter location:</label>
                <input type="text" id="location" name="location">
                <button type="submit">Search</button>
            </form>
        '''

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)


