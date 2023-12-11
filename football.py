print(
    "Hello and welcome to the new football league\nYour exercise is to add new teams to the league and name the league")

teams_dict = {}


def add_team():
    name_of_the_team = input("Enter the name of the team to add:")
    number_of_players = int(input("Enter the number of players this team has:"))
    most_famous_player = input("Enter the most famous player of this team:")
    if name_of_the_team not in teams_dict:
        teams_dict[name_of_the_team] = {"Players": number_of_players, "Famous player": most_famous_player}

    else:
        print("The team is already here!")


def change_team_name_and_players():
    old_team_name = input("Enter the old team name:")
    new_team_name = input("Enter the new name of the team to change:")
    new_amount_of_players = int(input("Enter the new players in the team:"))
    new_famous_player = input("Enter the newest most famous player on this team:")
    if old_team_name in teams_dict:
        teams_dict.pop(old_team_name)
        teams_dict[new_team_name] = {"Players": new_amount_of_players, "Famous player": new_famous_player}
    else:
        print("This team isn't in the teams table sorry!")


def search_team_name():
    name_to_search = input("Enter the name of the team to search:")
    if name_to_search in teams_dict:
        print(f"Name: {name_to_search}"
              f"\nPlayers: {teams_dict[name_to_search]['Players']}"
              f"\nMost famous player: {teams_dict[name_to_search]['Famous player']}")

    else:
        print("The team does not exists in our table!")


def remove_team():
    team_to_remove = input("Enter the team to remove:")
    if team_to_remove not in teams_dict:
        print("This team is not in here!")

    else:
        teams_dict.pop(team_to_remove)
        print(f"{team_to_remove} has been removed!")


# durev
def see_team_table():
    print("Let's see the teams in our table!")
    if teams_dict:
        for i in range(1, len(teams_dict) + 1):
            for name, players in teams_dict.items():
                print(
                    f"{i} Team name: {name}; Team players: {players['Players']}; Most famous player: {players['Famous player']}")
                break

    else:
        print("It seems like we have nothing in our table please go and add some teams!")


while True:
    print()
    print("1. Add team")
    print("2. Change team name and players")
    print("3. Search for team name")
    print("4. Remove team")
    print("5. See all teams table")
    print("6. Exit")
    num = int(input("Select a operation to do(1, 2, 3, 4, 5, 6):"))

    if num == 1:
        add_team()

    elif num == 2:
        change_team_name_and_players()

    elif num == 3:
        search_team_name()

    elif num == 4:
        remove_team()

    elif num == 5:
        see_team_table()

    elif num == 6:
        print("Exiting goodbye.....")
        break

    else:
        print("Invalid operation please enter a number(1, 2, 3, 4, 5)")
