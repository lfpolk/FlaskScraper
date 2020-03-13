from flask import Flask, render_template, url_for, request, redirect
import requests, bs4, sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
from datetime import datetime

app = Flask(__name__)
#Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fullstats.db'
db = SQLAlchemy(app)

#Create table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(40), nullable=False)
    corsiFor = db.Column(db.Integer, nullable=False)
    corsiAgainst = db.Column(db.Integer, nullable=False)
    gamesPlayed = db.Column(db.Integer, nullable=False)
    PPG = db.Column(db.Integer, nullable=False)
    PPO = db.Column(db.Integer, nullable=False)
    SHG = db.Column(db.Integer, nullable=False)
    SHO = db.Column(db.Integer, nullable=False)
    PPGA = db.Column(db.Integer, nullable=False)
    PPOA = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return'<Task %r>' % self.id


#Create class for each team to be an object of
class Team:

    #Static variable that keeps
    totalCorsi = 0


    def __init__(self, teamName, corsiFor, corsiAgainst, corsiFPercent, shotPercent, gamesPlayed, ppGoals, ppOpp, shGoals, shOpp, ppGAgainst, ppOppAgainst):
        self.teamName = teamName
        self.corsiFor = corsiFor
        self.corsiAgainst = corsiAgainst
        self.corsiFPercent = corsiFPercent
        self.shotPercent = shotPercent
        self.gamesPlayed= gamesPlayed
        self.ppGoals = ppGoals
        self.ppOpp = ppOpp
        self.shGoals = shGoals
        self.shOpp = shOpp
        self.ppGAgainst = ppGAgainst
        self.ppOppAgainst = ppOppAgainst


#Request URL from hockey-reference
ref = requests.get('https://www.hockey-reference.com/play-index/tpbp_finder.cgi?request=1&match=single&year_min=2020&year_max=2020&situation_id=5on5&order_by=corsi_for')

#Parse the HTML file
soup = bs4.BeautifulSoup(ref.text, 'html.parser')
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

        #Calculate corsi %
        CP = cFor / (cFor + cAgainst)

        #Get shooting %
        elem = soup.select(f'#stats > tbody > tr:nth-child({i}) > td:nth-child(10)')
        shotP = float(elem[0].text)

        #Create object for each team with corsi stats
        scrape_team = Team(team,cFor, cAgainst, CP, shotP, 0, 0, 0, 0, 0, 0, 0)
        list.append(scrape_team)

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

fox = requests.get('https://www.foxsports.com/nhl/team-stats?season=2019&category=SPECIAL+TEAMS&group=1&time=0&pos=0&team=1&page=1')
soup = bs4.BeautifulSoup(fox.text, 'html.parser')

NYI = 0
#Read each element from the table on fox sports
for i in range(1,32):

        #find where stats go in list
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td.wisbb_text.wisbb_fixedColumn > div > span:nth-child(3)')
        team = elem[0].text
        if team == 'New York':
            if NYI == 1:
                team = team + ' Islanders'
            NYI += 1
        for city in list:
            if (city.teamName.startswith(team)):
                index = list.index(city)

        #Get Games Played
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(2)')
        GP = int(elem[0].text)

        #Get PP goals
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(3)')
        ppG = int(elem[0].text)

        #Get PP opportunities
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(4)')
        ppO = int(elem[0].text)

        #Get SH goals
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(6)')
        shG = int(elem[0].text)

        #Get SH opportunities
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(7)')
        shO = int(elem[0].text)

        #Get PP GA
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(9)')
        ppGA = int(elem[0].text)

        #Get PP opportunites against
        elem = soup.select(f'#wisfoxbox > section.wisbb_body > div.wisbb_expandableTable.wisbb_teamFixed.wisbb_statsTable > table > tbody > tr:nth-child({i}) > td:nth-child(10)')
        ppOA = float(elem[0].text)

        #Update list with PP stats
        list[index].gamesPlayed = GP
        list[index].ppGoals = ppG
        list[index].ppOpp = ppO
        list[index].shGoals = shG
        list[index].shOpp = shO
        list[index].ppGAgainst = ppGA
        list[index].ppOppAgainst = ppOA

corsiFor = sum(c.corsiFor for c in list)
corsiAgainst = sum(c.corsiAgainst for c in list)
corsiFPercent = sum(c.corsiFPercent for c in list)
shotPercent = sum(c.shotPercent for c in list)
gamesPlayed = sum(c.gamesPlayed for c in list)
ppGoals = sum(c.ppGoals for c in list)
ppOpp = sum(c.ppOpp for c in list)
shGoals = sum(c.shGoals for c in list)
shOpp = sum(c.shOpp for c in list)
ppGAgainst = sum(c.ppGAgainst for c in list)
ppOppAgainst = sum(c.ppOppAgainst for c in list)

leagueAVG = Team('League Average',corsiFor/31, corsiAgainst/31, corsiFPercent/31, shotPercent/31, gamesPlayed/31, ppGoals/31, ppOpp/31, shGoals/31, shOpp/31, ppGAgainst/31, ppOppAgainst/31)
list.append(leagueAVG)
teams = Todo.query.order_by(Todo.teamName).all()
if len(teams) < 32:
    for i in teams:
        db.session.delete(i)
        db.session.commit()
    for i in range(0,32):
        new_team = Todo(teamName=list[i].teamName,corsiFor= list[i].corsiFor/list[i].gamesPlayed, corsiAgainst=list[i].corsiAgainst/list[i].gamesPlayed, gamesPlayed=list[i].gamesPlayed, PPG = list[i].ppGoals / list[i].gamesPlayed, PPO = list[i].ppOpp / list[i].gamesPlayed, SHG = list[i].shGoals / list[i].gamesPlayed, SHO = list[i].shOpp / list[i].gamesPlayed, PPGA = list[i].ppGAgainst / list[i].gamesPlayed, PPOA = list[i].ppOppAgainst / list[i].gamesPlayed)
        db.session.add(new_team)
        db.session.commit()

if len(teams) > 32:
    for i in teams:
        db.session.delete(i)
        db.session.commit()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/stats')
def stats():
    teams = Todo.query.order_by(Todo.teamName).all()
    return render_template('stats.html', teams=teams)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/PPstats')
def PPstats():
    teams = Todo.query.order_by(Todo.teamName).all()
    return render_template('PPstats.html', teams=teams)

if __name__ == "__main__":
    app.run(debug=True)