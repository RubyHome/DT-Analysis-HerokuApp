import json
#from apps.core.models import Game, Team

__author__ = 'rickporter'


import csv


#gl/sy goal line short yardage
def get_name(k):
    return k.split('.')[-1].lower()

def print_field(key, row):
    print(k + ": " + row[k])

with open('data/IL Games/1608 IL DEF VS MN 10-29-16.csv', 'r') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader = csv.DictReader( csvfile )
    game = {}
    game['name'] = '1608 IL DEF VS MN 10-29-16'
    game['date'] = '10-29-16'
    game[''] = ''
    game['plays'] = []
    for row in reader:
        #print(row)

        play = {}
        game['plays'].append(play)
        play['sequence'] = row['GameSegment.PlayNumber']
        play['name'] = row['Name']
        play['quarter'] = row['Play.Quarter']


        defense = {}
        play['defense'] = defense

        stats = {}
        play['stats'] = stats

        for k in row:
            if k.startswith('Play.Defense'):
                defense[get_name(k)] = row[k]
            elif k.startswith('Football.'):
                stats[get_name(k)] = row[k]
            elif k.startswith('Play.Shared'):
                play[get_name(k)] = row[k]

            #if k == 'Play.Shared.GL/SY':
            #    print_field(k, row)




print(json.dumps(game,sort_keys=True,indent=4, separators=(',', ': ')))



#Load NCAA Data


#def create_team(short_name):
#    t = Team()
#    t.short_name = short_name
#    t.name = short_name

#g = Game()

#g.game_date = game['date']
#g.name = game['name']





