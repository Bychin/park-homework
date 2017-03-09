import os
import sys
import random

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch
getch = _find_getch()

def _exit():
    os.system("cls") #clear
    print("Goodbye!")
    sys.exit()

def _return_to_main():
    print("\nPress any key to return to the main menu...")
    in_ch = ord(getch())
    if in_ch != None:
        os.system("cls") #clear
    else:
        _exit()

if __name__ == "__main__":
    print("Welcome to the Champions League!\n")
    

    while True:
        print("Select an option by entering a number: \n")
        print("1) Play!")
        print("2) Show all teams")
        print("3) Change teams")
        print("4) Exit")

        in_ch = ord(getch())

        if in_ch == 49: # 1) Play!
            os.system("cls") #clear
            random.seed()
            team_list = []
            tmp_teams = set()
            file = open("commands_list.txt", "r")
            for line in file:
                team_list.append(line[:-1])
                tmp_teams.add(line[:-1])
            file.close()

            stage = 8
            file = open("history.txt", "w")

            while stage >= 1:

                numb_list = [l for l in range(16)] # for random
                print(("---Stage {}---\n".format(stage)))
                file.write("---Stage {}---\n".format(stage))
                left_side = []
                right_side = []

                for i in range(stage):

                    idx1 = random.choice(numb_list)
                    while (team_list[idx1] == "-"):
                        idx1 = random.choice(numb_list)
                    numb_list.remove(idx1)

                    idx2 = random.choice(numb_list)
                    while (team_list[idx2] == "-"):
                        idx2 = random.choice(numb_list)
                    numb_list.remove(idx2)

    
                    left_side.append(team_list[idx1])
                    right_side.append(team_list[idx2])

                    score_left = random.randint(0, 6)
                    score_right = random.randint(0, 6)
                    while (score_left == score_right):
                        score_right = random.randint(0, 6)

                    file.write("{} vs {}: {} - {}\n".format(left_side[i], right_side[i],
                                                          score_left, score_right))
                    print("{} vs {}: {} - {}\n".format(left_side[i], right_side[i],
                                                       score_left, score_right))
                    if score_left > score_right:
                        team_list[idx2] = "-"
                    else:
                        team_list[idx1] = "-"

                stage //= 2

            file.close()

            print("Do you want to see the path of a particular team? [Y/N]")
            in_ch = ord(getch())
            while in_ch == 89 or in_ch == 121:
                team_name = input("Enter team's name: ")

                if team_name in tmp_teams:
                    file = open("history.txt", "r")
                    team_list = tuple(file.readlines())
                    stg = 8
                    for str in team_list:
                        if team_name in str:
                            print("Stage {}: {}".format(stg, str[:-1]))
                            stg //= 2
                    file.close()
                
                else:
                    print("No such team!")
                print("Do you want to see more? [Y/N]")
                in_ch = ord(getch())
            os.system("cls") #clear

        elif in_ch == 50: # 2) Show all teams
            os.system("cls") #clear
            file = open("commands_list.txt", "r")
            team_list = tuple(file.readlines())
            for team in team_list:
                print(team[:-1])
            file.close()

            _return_to_main()
            

        elif in_ch == 51: # 3) Change teams
            os.system("cls") #clear
            print("Warning: next steps will delete all previous data!\nContinue? [Y/N]")
            in_ch = ord(getch())

            if in_ch == 89 or in_ch == 121:

                os.system("cls") #clear
                print("Your must enter 16 teams in total:\n")

                file = open("commands_list.txt", "w")
                for team in range(16):
                    print("Enter team #{}: ".format(team + 1))
                    file.write(input())
                    file.write('\n')
                file.close()

                _return_to_main()

            else:
                os.system("cls") #clear

        elif in_ch == 52: # 4) Exit
            _exit()

        else:
            os.system("cls") #clear
        