players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]
class Player:
    players_list = []
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        Player.players_list.append(self)

    @classmethod
    def display_players(cls):
        i=1
        for player in cls.players_list:
             print(f"player {i} \nName : {player.name}\nAge:{player.age} \nPosition : {player.position}\nTeam : {player.team}")
             i+=1
i=1
for player in players:
    player_c = Player(player["name"], player["age"], player["position"], player["team"])
    print(f"player {i} \nName : {player_c.name}\nAge:{player_c.age} \nPosition : {player_c.position}\nTeam : {player_c.team}")
    i+=1
    print("-"*50)

print("*"*100)
Player.display_players()