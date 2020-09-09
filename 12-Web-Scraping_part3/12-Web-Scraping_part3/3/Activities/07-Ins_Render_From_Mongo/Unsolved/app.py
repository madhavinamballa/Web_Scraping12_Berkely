from flask import Flask, render_template
import pymongo
app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.team_db
db.team.drop()
db.team.insert_many(
    [
        {
            'player': 'Jessica',
            'position': 'Point Guard'
        },
        {
            'player': 'Mark',
            'position': 'Center'
        }
        {
           'player': 'Mick',
            'position': 'off-center' 
        }
    ]
)
@app.route('/')
def index():
    team=list(db.team.find())
    print(team)
    return render_template('index.html', teams=team)

if __name__ == "__main__":
    app.run(debug=True)