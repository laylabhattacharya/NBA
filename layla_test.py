import json
from nba_api.stats.endpoints import teamvsplayer
from nba_api.stats.static import players, teams

def search_player():
    player_name = input("Enter the player's full name: ").strip()
    player_data = players.find_players_by_full_name(player_name)
    if player_data:
        player = player_data[0]
        print(f"Found Player: {player['full_name']} (ID: {player['id']})")
        return player['id']
    else:
        print("Player not found. Please try again.")
        return None

def search_team():
    team_name = input("Enter the team name: ")
    team_data = teams.find_team_by_abbreviation(team_name)
    if team_data:
        team = team_data
        print(f"Found Team: {team['full_name']} (ID: {team['id']})")
        return team['id']
    else:
        print("Team not found. Please try again.")
        return None
def main():
    player_id = search_player()
    team_id = search_team()
    gamesdata = teamvsplayer.TeamVsPlayer(team_id=team_id, vs_player_id=player_id).get_dict()
    games = gamesdata['resultSets'][0]['rowSet']
    print("Data Found.")
    # hi everyone


if __name__ == "__main__":
    main()
