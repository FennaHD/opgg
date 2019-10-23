from django.shortcuts import render
from django.http import HttpResponse
import requests
from numeral import roman2int

# Create your views here.

access_key = "RGAPI-1b6ebad3-5ada-4957-830f-6ab53dd70c88"

def homepage(request):
    return render(request=request, template_name="main/home.html")
    # I can add a context parameter to render as such: context={"tutorials": Tutorial.objects.all()}
    # this would basically mean that you're adding information from the database to feed to the template. 
    # in this case I have a model set up but didn't create a table, so I have nothing to add
    # when I have something to store then I can add the parameter
    
def summoner(request):
    summoner_name = request.GET["summoner_name"]
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}"

    summoner_data = requests.get(url.format(summoner_name, access_key)).json()

    summoner_icon_id = summoner_data['profileIconId']
    summoner_level = summoner_data['summonerLevel']
    summoner_id = summoner_data['id']
    account_id = summoner_data['accountId']

    rank, league_points, wins, losses, win_ratio = getTierInfo(summoner_id)

    matches = getMatchList(account_id)

    fav_champs_ids = getMainChamp(summoner_id)

    context = { 'name':summoner_name,
                'icon':summoner_icon_id, 
                'level':summoner_level,
                'id':summoner_id,
                'account_id':account_id,
                'matches':matches,
                'fav_champs_ids':fav_champs_ids,
                'rank': rank,
                'league_points': league_points,
                'wins': wins,
                'losses': losses,
                'win_ratio': win_ratio
              }

    return render(request=request, template_name="main/summoner.html", context=context)

#use this function to get a list of matches of the player
def getMatchList(account_id):
    url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?api_key={}&endIndex={}"
    match_json = requests.get(url.format(account_id, access_key, 10)).json()
    matches = match_json['matches']

    return matches

def getMainChamp(summoner_id):
  url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}"
  champion_list = requests.get(url.format(summoner_id, access_key)).json()
  fav_champ_ids = []
  for champion in champion_list[:7]:
    fav_champ_ids.append(champion["championId"])
    
  return fav_champ_ids

def getTierInfo(summoner_id):
  url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}"
  tier_info = requests.get(url.format(summoner_id, access_key)).json()
  rank = (tier_info[0]["tier"] + " " + str(roman2int(tier_info[0]["rank"]))).title()
  league_points = tier_info[0]["leaguePoints"]
  wins = tier_info[0]["wins"]
  losses = tier_info[0]["losses"]
  win_ratio = str(int(round((int(wins) * 100)/(int(wins) + int(losses))))) 
  return rank, league_points, wins, losses, win_ratio
