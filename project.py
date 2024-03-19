import requests
import random
def get_random_pokemon_id():
    return random.randint(1, 151)
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'attack': pokemon_data['stats'][1]['base_stat'],
            'defense': pokemon_data['stats'][2]['base_stat'],
            'speed': pokemon_data['stats'][3]['base_stat'],
            'types': [t['type']['name'] for t in pokemon_data['types']]
        }
    else:
        raise Exception(f"Error fetching Pokemon data. Status code: {response.status_code}")

def print_pokemon_info(pokemon):
    print(
        f"\n{pokemon['name'].capitalize()} (ID: {pokemon['id']}) - Height: {pokemon['height']} decimetres, Weight: {pokemon['weight']} hectograms")
    print(f"Types: {', '.join(pokemon['types'])}")
    print("""
           _.-=-.
         .'      '.
        /          \
        |          ;
         \        //
          \      //
          |     ||
        \_|     ||
        \/  -_- \/
          |   |  
          |   |   
          |   |   
""")


def compare_stats(player_name, player_stat, opponent_name, opponent_stat, stat_name):
    if player_stat > opponent_stat:
        print(f"{player_name} win! {player_name} has a higher {stat_name}.")
        return 1
    elif player_stat < opponent_stat:
        print(f"{player_name} lose! {opponent_name} has a higher {stat_name}.")
        return -1
    else:
        print(f"It's a tie! Both have the same {stat_name}.")
        return 0


def play_game():
    player_score = 0
    opponent_score = 0
    rounds = 0

    while rounds < 3:  # Play 3 rounds
        player_pokemon_id = get_random_pokemon_id()
        player_pokemon = get_pokemon_data(player_pokemon_id)

        opponent_pokemon_id = get_random_pokemon_id()
        opponent_pokemon = get_pokemon_data(opponent_pokemon_id)

        if player_pokemon and opponent_pokemon:
            print("\nRound", rounds + 1)
            print("\nWelcome to Pokemon Top Trumps!")
            print_pokemon_info(player_pokemon)

            stat_choice = input("Choose a stat (id, height, weight, attack, defense, speed): ").lower()

            if stat_choice in ('id', 'height', 'weight', 'attack', 'defense', 'speed'):
                player_stat = player_pokemon[stat_choice]
                opponent_stat = opponent_pokemon[stat_choice]

                print_pokemon_info(opponent_pokemon)
                result = compare_stats("You", player_stat, "Your opponent", opponent_stat, stat_choice)

                if result == 1:
                    player_score += 1
                elif result == -1:
                    opponent_score += 1

                rounds += 1

            else:
                print("Invalid choice. Please choose id, height, weight, attack, defense, or speed.")

    print("\nGame Over!")
    print("Your Score:", player_score)
    print("Opponent's Score:", opponent_score)
    if player_score > opponent_score:
        print("""
    ________    
   /        \    
  |  Victory |   
   \        /   
    \______/
""")
        print("Congratulations! You win!")
    elif player_score < opponent_score:
        print("""
    ________    
   /        \    
  |  Defeat |   
   \        /   
    \______/
""")
        print("Sorry, you lose. Better luck next time!")
    else:
        print("""
    ________    
   /        \    
  |   Draw  |   
   \        /   
    \______/
""")
        print("It's a draw!")


if __name__ == "__main__":
    print(
        "Welcome to Top Trumps! Here are the instructions: You are given a random card with different stats, and you select one of the card's stats. Another random card is selected for your opponent (the computer). The stats of the two cards are compared. The player with the stat higher than their opponent wins")

    continue_game = input("Would you like to play? Answer yes if so. ")

    if continue_game.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")


