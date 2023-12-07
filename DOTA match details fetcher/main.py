

import requests
from pprint import pprint

key = "18EC2CB1471BAEB5D7ED0FFB4AD2F4DA"
sherry_steam_id = 76561198362197783
app_id = 570
my_steam_id = 76561198344201628
sherry_dota_game_id = 165678888
haris = 243816705

# getting last match played by the player
open_api_url = f"https://api.opendota.com/api/players/{haris}/matches?limit=1"
# making a request to the open api servers
response = requests.get(open_api_url)
# storing match id
json_format = response.json()
sherry_match_details = {
    "last_match_id": json_format[0]['match_id'],
    "duration": json_format[0]['duration'],
    "avg_rank":json_format[0]['average_rank']
}

# now constructing url for the match details
match_details_url = f"https://api.steampowered.com/IDOTA2MATCH_570/GetMatchDetails/v1/?key={key}&match_id={int(sherry_match_details['last_match_id'])}&skill"
# making a request to servers
response = requests.get(match_details_url)
json_format = response.json()
# storing player details that i want to extract
player_details_that_i_want = {
    'radiant_score':json_format['result']['radiant_score'],
    "dire_score":json_format['result']['dire_score'],
    'players_list':json_format['result']['players']
}

for player in player_details_that_i_want['players_list']:
    for item in player.values():
        if item == haris:
            player_details_that_i_want['player_khaata'] = player


# now need to write these on a file
with open("khaata.txt", "w") as f:
    f.write("Match ID: " + str(sherry_match_details['last_match_id']) + '\n')
    f.write("Duration: " + str((sherry_match_details['duration'] / 60)) + "\n")
    f.write("Average Rank: " + str(sherry_match_details['avg_rank']) + '\n')
    if player_details_that_i_want['player_khaata']['team_number'] == 0:
        # it means radiant
        f.write("Player Team: Radiant\n")
    elif player_details_that_i_want['player_khaata']['team_number'] == 1:
        # it means dire
        f.write("Player Team: Dire\n")
    f.write(f"Radiant Score: {player_details_that_i_want['radiant_score']}\n")
    f.write(f"Dire Score: {player_details_that_i_want['dire_score']}\n")

    f.write("Player Stats: \n")
    f.write(f"Kills: {player_details_that_i_want['player_khaata']['kills']}, Deaths: {player_details_that_i_want['player_khaata']['deaths']}, Assists {player_details_that_i_want['player_khaata']['assists']}\n")
    f.write(f"Abandoned: {player_details_that_i_want['player_khaata']['leaver_status']}\n")
    f.write(f"Last Hits: {player_details_that_i_want['player_khaata']['last_hits']}, Denies: {player_details_that_i_want['player_khaata']['denies']}\n")
    f.write(f"Networth: {player_details_that_i_want['player_khaata']['net_worth']}, GPM: {player_details_that_i_want['player_khaata']['gold_per_min']}, XPM: {player_details_that_i_want['player_khaata']['xp_per_min']}"
            f" , Level: {player_details_that_i_want['player_khaata']['level']}\n")
    f.write(f"Hero Damage Dealt: {player_details_that_i_want['player_khaata']['hero_damage']}, Tower Damage Dealt: {player_details_that_i_want['player_khaata']['tower_damage']}\n")

