var logo = [
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
    ];
    function simulate() {
      var homeTeam = document.getElementById("homeTeam").value;
      var awayTeam = document.getElementById("awayTeam").value;
      var homePercentage = 0;
      if (homeTeam == awayTeam) {
        document.getElementById("sameTeam").innerHTML = "Teams can't play themselves";
      }
      else {
      homePercentage =  Math.round((Math.random() * 40)) + 30;
      document.getElementById("homeWPercent").innerHTML = homePercentage + "%";
      document.getElementById("awayWPercent").innerHTML = (100 - homePercentage) + "%";
    
      }
    }
    
    function changeHomeImage() {
      document.getElementById("home-logo").src = logo[document.getElementById("homeTeam").value];
      document.getElementById("homeWPercent").innerHTML = " ";
      document.getElementById("awayWPercent").innerHTML = " ";
    }
    
    function changeAwayImage() {
      document.getElementById("away-logo").src = logo[document.getElementById("awayTeam").value];
      document.getElementById("homeWPercent").innerHTML = " ";
      document.getElementById("awayWPercent").innerHTML = " ";
    }
    