from flask import Flask, render_template, url_for, request, redirect
import requests, bs4, sys
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
db = SQLAlchemy(app)

#Create table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(40), nullable=False)
    corsiFor = db.Column(db.Integer, nullable=False)
    corsiAgainst = db.Column(db.Integer, nullable=False)
    gamesPlayed = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return'<Task %r>' % self.id

#Create class for each team to be an object of
class Team:

    #Static variable that keeps
    totalCorsi = 0


    def __init__(self, teamName, corsiFor, corsiAgainst):
        self.teamName = teamName
        self.corsiFor = corsiFor
        self.corsiAgainst = corsiAgainst

#Request URL from hockey-reference
res = requests.get('https://www.hockey-reference.com/play-index/tpbp_finder.cgi?request=1&match=single&year_min=2020&year_max=2020&situation_id=5on5&order_by=corsi_for')

#Parse the HTML file
soup = bs4.BeautifulSoup(res.text, 'html.parser')
list = []
#Read each element from the table on hockey reference into objects
for i in range(1,33):
    if i != 21: # No data on row 20 on hockey-reference

        #Get team name abbreviation
        elem = soup.select(f'#stats > tbody > tr:nth-child({i}) > td:nth-child(2)')
        team = elem[0].text

        #Get Corsi for
        elem = soup.select(f'#stats > tbody > tr:nth-child({i}) > td:nth-child(4)')
        cFor = int(elem[0].text)

        #Get Corsi against
        elem = soup.select(f'#stats > tbody > tr:nth-child({i}) > td:nth-child(5)')
        cAgainst = int(elem[0].text)

        #Create object for each team with corsi stats
        globals()[team] = Team(team,cFor, cAgainst)
        Team.totalCorsi = Team.totalCorsi + cFor
        list.append(globals()[team])

list.sort(key=lambda x: x.teamName)
#Swap to order by team name, not abr
list[16], list[17] = list[17], list[16]
list[4], list[6] = list[6], list[4]
list[5], list[6] = list[6], list[5]
list[6], list[7] = list[7], list[6]
list[7], list[8] = list[8], list[7]



teamNum = -1

list[0].teamName = "Anaheim Ducks"
list[1].teamName = "Arizona Coyotes"
list[2].teamName = "Boston Bruins"
list[3].teamName = "Buffalo Sabres"
list[4].teamName = "Calgary Flames"
list[5].teamName = "Carolina Hurricanes"
list[6].teamName = "Chicago Blackhawks"
list[7].teamName = "Colorado Avalanche"
list[8].teamName = "Columbus Blue Jackets"
list[9].teamName = "Dallas Stars"
list[10].teamName = "Detroit Red Wings"
list[11].teamName = "Edmonton Oilers"
list[12].teamName = "Florida Panthers"
list[13].teamName = "Los Angeles Kings"
list[14].teamName = "Minnesota Wild"
list[15].teamName = "Montreal Canadiens"
list[16].teamName = "Nashville Predators"
list[17].teamName = "New Jersey Devils"
list[18].teamName = "New York Islanders"
list[19].teamName = "New York Rangers"
list[20].teamName = "Ottawa Senators"
list[21].teamName = "Philadelphia Flyers"
list[22].teamName = "Pittsburgh Penguins"
list[23].teamName = "San Jose Sharks"
list[24].teamName = "St. Louis Blues"
list[25].teamName = "Tampa Bay Lightning"
list[26].teamName = "Toronto Maple Leafs"
list[27].teamName = "Vancouver Canucks"
list[28].teamName = "Vegas Golden Knights"
list[29].teamName = "Washington Capitals"
list[30].teamName = "Winnipeg Jets"

teams = Todo.query.order_by(Todo.teamName).all()
if len(teams) < 1:
    for i in range(30):
        new_team = Todo(teamName=list[i].teamName,corsiFor=list[i].corsiFor,corsiAgainst=list[i].corsiAgainst,gamesPlayed=60)

        db.session.add(new_team)
        db.session.commit()
print(len(teams))

s
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/stats')
def stats():
    return render_template('stats.html', teams=teams)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        task_to_delete = Todo.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        teams = Todo.query.order_by(Todo.teamName).all()
        return render_template('stats.html',teams=teams)
    except:
        return 'There was a problem deleting the task'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)