from flask import Flask, render_template, url_for, request, redirect
import requests, bs4, sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

#Create Database
ENV ='prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://larsonpolk:dukey@localhost/nhlpredictor'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cpufndielzwofq:cfb198efddab3d1bc845d381863043621aad0fbcfe3db2677066067c734d7907@ec2-35-171-31-33.compute-1.amazonaws.com:5432/dbr9llf5fr0qns'

db = SQLAlchemy(app)

#Create table
class Stats(db.Model):

    __tablename__ = 'Stats'
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(40), nullable=False)
    corsiFor = db.Column(db.Float, nullable=False)
    corsiAgainst = db.Column(db.Float, nullable=False)
    gamesPlayed = db.Column(db.Float, nullable=False)
    shotP = db.Column(db.Float, nullable=False)
    PPG = db.Column(db.Float, nullable=False)
    PPO = db.Column(db.Float, nullable=False)
    SHG = db.Column(db.Float, nullable=False)
    SHO = db.Column(db.Float, nullable=False)
    PPGA = db.Column(db.Float, nullable=False)
    PPOA = db.Column(db.Float, nullable=False)

    def __init__(self, id, teamName, corsiFor, corsiAgainst, gamesPlayed, shotP, PPG, PPO, SHG, SHO, PPGA, PPOA):
        self.id = id
        self.teamName = teamName
        self.corsiFor = corsiFor
        self.corsiAgainst = corsiAgainst
        self.gamesPlayed = gamesPlayed
        self.shotP = shotP
        self.PPG = PPG
        self.PPO = PPO
        self.SHG = SHG
        self.SHO = SHO
        self.PPGA = PPGA
        self.PPOA = PPOA

""" To do
class Goalie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(3), nullable=False)
    goalieName = db.Column(db.String(40), nullable=False)
    saveP = db.Column(db.Integer, nullable=False)

    

    def __repr__(self):
        return'<Task %r>' % self.id
"""
#Create class for each team to be an object of
class Team:

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

"""
class goalie:

    def __init__(self, tName, gName, SVP):
        self.tName = tName
        self.gName = gName
        self.SVP = SVP

#Request URL for goalie stats from NHL
gref = requests.get('http://www.nhl.com/stats/goalies?reportType=season&seasonFrom=20192020&seasonTo=20192020&gameType=2&filter=gamesPlayed,gte,1&filter=shotsAgainst,gte,400&sort=a_teamAbbrevs&page=0&pageSize=62')
soup = bs4.BeautifulSoup(gref.text, 'html.parser')
goalies = []

for i in range(70):
        elem = soup.select(f'#root > main > div.ReactTable.-striped.-highlight.rthfc-k8c2qqcu.rthfc.-sp > div.rt-table > div.rt-tbody > div:nth-child({i})')
        print(elem)
        name = elem[0].text
        print(elem)
        print(name)
"""

logo = [
        "",
        "https://cdn.freebiesupply.com/logos/large/2x/anaheim-ducks-logo.png",
        "https://nhl.bamcontent.com/images/assets/binary/309994320/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/301172494/binary-file/file.svg",
        "https://www-league.nhlstatic.com/images/logos/teams-current-circle/7.svg",
        "https://www-league.nhlstatic.com/images/logos/teams-current-circle/20.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-12-light.svg",
        "https://nhl.bamcontent.com/images/assets/binary/301971744/binary-file/file.svg",
        "https://www-league.nhlstatic.com/images/logos/teams-current-primary-dark/21.svg",
        "https://nhl.bamcontent.com/images/assets/binary/301936032/binary-file/file.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-25-dark.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-17-light.svg",
        "https://nhl.bamcontent.com/images/assets/binary/290013862/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/291015530/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/308180580/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/302317224/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/309964716/binary-file/file.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-18-dark.svg",
        "https://nhl.bamcontent.com/images/assets/binary/301891622/binary-file/file.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-2-secondary-light.svg",
        "https://nhl.bamcontent.com/images/assets/binary/289471614/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/299813882/binary-file/file.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-4-light.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1581615643/images/logos/team/current/team-5-light.svg",
        "https://nhl.bamcontent.com/images/assets/binary/301041748/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/309991890/binary-file/file.svg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSN4N59kymrO2JuS7vcdruceVzpm0ounWR-5N9RMwu9ITZg8VHx",
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Toronto_Maple_Leafs_2016_logo.svg/1200px-Toronto_Maple_Leafs_2016_logo.svg.png",
        "https://nhl.bamcontent.com/images/assets/binary/309954422/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/290581542/binary-file/file.svg",
        "https://nhl.bamcontent.com/images/assets/binary/298789884/binary-file/file.svg",
        "https://www-league.nhlstatic.com/nhl.com/builds/site-core/15a57250ae5ef77e77d0aeb2f5dfb813067e4885_1583360821/images/logos/team/current/team-52-dark.svg"
        ]

def scrape():
    global teams
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
    list[29], list[30] = list[30], list[29]



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
    teams = Stats.query.order_by(Stats.teamName).all()
    print(teams)
    for i in teams:
        db.session.delete(i)
        db.session.commit()
    for i in range(0,32):
        new_team = Stats(id=i+1,teamName=list[i].teamName,corsiFor= list[i].corsiFor/list[i].gamesPlayed, corsiAgainst=list[i].corsiAgainst/list[i].gamesPlayed, gamesPlayed=list[i].gamesPlayed, shotP=list[i].shotPercent, PPG = list[i].ppGoals / list[i].gamesPlayed, PPO = list[i].ppOpp / list[i].gamesPlayed, SHG = list[i].shGoals / list[i].gamesPlayed, SHO = list[i].shOpp / list[i].gamesPlayed, PPGA = list[i].ppGAgainst / list[i].gamesPlayed, PPOA = list[i].ppOppAgainst / list[i].gamesPlayed)
        db.session.add(new_team)
        db.session.commit()

@app.route('/', methods=['POST', 'GET'])
def index():
        teams = Stats.query.order_by(Stats.teamName).all()
        print(teams)
        return render_template('index.html',teams=teams)


@app.route('/stats', methods=['POST', 'GET'])
def stats():
    if request.method == 'POST':
        teams = Stats.query.order_by(Stats.teamName).all()
        return render_template('stats.html', teams=teams)
    else:
        teams = Stats.query.order_by(Stats.teamName).all()
        return render_template('stats.html', teams=teams)

@app.route('/PPstats')
def PPstats():
    teams = Stats.query.order_by(Stats.teamName).all()
    return render_template('PPstats.html', teams=teams)

@app.route('/simulation', methods=['POST', 'GET'])
def simulation():
    teams = Stats.query.all()
    if request.method == 'POST':
        home = int(request.form.get('homeTeam'))
        away = int(request.form.get('awayTeam'))
        ht = teams[home-1]
        at = teams[away-1]
        avg=teams[31]

        #Calculate expected shots
        hShots = ((ht.corsiFor - avg.corsiFor) + (at.corsiAgainst - avg.corsiAgainst) + avg.corsiAgainst) * 0.85
        aShots = ((at.corsiFor - avg.corsiFor) + (ht.corsiAgainst - avg.corsiAgainst) + avg.corsiAgainst) * 0.85

        #Calculate even strength goals
        #Replace hSvP and aSvP when goalie stats are accessible
        hSvP = .91
        aSvP = .91
        hMultiplier = 1.0436
        aMultiplier = .9564
        hESG = (hShots * ((ht.shotP/100 + 1-aSvP)/2) * .85) * hMultiplier
        aESG = (aShots * ((at.shotP/100 + 1-hSvP)/2) * .85) * aMultiplier
        
        #Calulate power play attempts
        hPPX = 1.034808419
        aPPX = 0.965191581
        hPPA = ((ht.PPO - avg.PPO) + (at.PPOA - avg.PPOA) + avg.PPO) * hPPX
        aPPA = ((at.PPO - avg.PPO) + (ht.PPOA - avg.PPOA) + avg.PPO) * aPPX

        #Calculate Goals per attempt
        hGPA = ht.PPG / ht.PPO
        aGPA = at.PPG / at.PPO
        lGPA = avg.PPG / avg.PPO

        #Calculate goals per attempt against
        hGPAA = ht.PPGA / ht.PPOA
        aGPAA = at.PPGA / at.PPOA

        #Calculate expected goals
        hPPG = (((hGPA - lGPA) + (aGPAA - lGPA) + lGPA) * hPPA)
        aPPG = (((aGPA - lGPA) + (hGPAA - lGPA) + lGPA) * aPPA)

        #Calculate total goals
        hXG = hPPG + hESG
        aXG = aPPG + aESG

        #Calculate pythagenpat exponent
        pythagenpat = (hXG + aXG) ** .458

        #Calculate win percentage
        hWP = hXG ** pythagenpat / (aXG ** pythagenpat + hXG ** pythagenpat)
        aWP = aXG ** pythagenpat / (hXG ** pythagenpat + aXG ** pythagenpat)

        return render_template('simulation.html', home=teams[home-1], away=teams[away-1], avg=avg, awayLogo = logo[away], homeLogo = logo[home], hShots=hShots, aShots=aShots, hESG=hESG, aESG=aESG, hPPG=hPPG, aPPG=aPPG, hXG=hXG, aXG=aXG, hWP=hWP, aWP=aWP)

if __name__ == "__main__":
    app.debug = True
    app.run()