import json
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog, scoreboardv2

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

def get_player_games(player_id):
    try:
        season = input("Enter the season year (e.g., 2023 for 2023-24 season): ").strip()
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season).get_dict()
        games = gamelog['resultSets'][0]['rowSet']
        if not games:
            print("No games found for the specified player and season.")
            return

        print(f"\nGames for Player ID {player_id} in Season {season}:")
        for game in games:
            print(f"Game Date: {game[3]}, Matchup: {game[4]}, Points: {game[24]}, Assists: {game[19]}, Rebounds: {game[18]}")
    except Exception as e:
        print(f"Error fetching player game logs: {e}")

def view_scoreboard():
    try:
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        scoreboard_data = scoreboardv2.ScoreboardV2(game_date=date).get_dict()
        games = scoreboard_data['resultSets'][0]['rowSet']
        if not games:
            print("No games found for the specified date.")
            return

        print(f"\nNBA Games on {date}:")
        for game in games:
            print(f"Game: {game[5]} vs {game[7]}, Time: {game[9]}, Arena: {game[15]}")
    except Exception as e:
        print(f"Error fetching scoreboard: {e}")

def main():
    while True:
        print("\nNBA Info Application")
        print("1. Search for a player")
        print("2. View player's game logs")
        print("3. View scoreboard")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            player_id = search_player()
        elif choice == '2':
            if 'player_id' not in locals() or not player_id:
                print("You need to search for a player first.")
            else:
                get_player_games(player_id)
        elif choice == '3':
            view_scoreboard()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
