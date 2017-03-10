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
    import tty
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
    os.system("clear") 
    print("Goodbye!")
    sys.exit()


def _return_to_main():
    print("\nPress any key to return to the main menu...")
    in_ch = ord(getch())
    if in_ch != None:
        os.system("clear") 
    else:
        _exit()


def _stage_play(stg):
    while stg >= 1:

        if stg != 1:
            print("\n---Stage 1/{}---\n".format(stg))
            file.write("---Stage 1/{}---\n".format(stg))
        else:
            print("\n---Final---\n")
            file.write("---Final---\n")

        for i in range(stg):

            left_side = team_list.pop()
            right_side = team_list.pop()

            score_left = random.randint(0, 6)
            score_right = random.randint(0, 6)

            file.write("{} vs {}: {} - {}\n".format(left_side, right_side,
                                                    score_left, score_right))
            print("{} vs {}: {} - {}".format(left_side, right_side,
                                             score_left, score_right))
            if score_left > score_right:
                tmp_teams.remove(right_side)
            elif score_left < score_right:
                tmp_teams.remove(left_side)
            else:
                pen_score_left = random.randint(0, 6)
                pen_score_right = random.randint(0, 6)
                while (pen_score_left == pen_score_right):
                    pen_score_right = random.randint(0, 6)
                file.write("(Penalty: {} - {})\n".format(pen_score_left, pen_score_right))
                print("(Penalty: {} - {})".format(pen_score_left, pen_score_right)) 

                if pen_score_left > pen_score_right:
                    tmp_teams.remove(right_side)
                elif pen_score_left < pen_score_right:
                    tmp_teams.remove(left_side)

            team_list.update(tmp_teams)
            stg //= 2


if __name__ == "__main__":
    os.system("clear")
    print("Welcome to the Champions League!\n")
    

    while True:
        print("Select an option by entering a number: \n")
        print("1) Play!")
        print("2) Show all teams")
        print("3) Change teams")
        print("4) Exit")

        in_ch = ord(getch())

        if in_ch == 49: # 1) Play! (49 == '1')
            os.system("clear")
            random.seed()
            file = open("commands_list.txt", "r")
            team_list = set()
            tmp_teams = set()
            for line in file:
                if (line == "\n"):
                    continue
                team_list.add(line[:-1])
                tmp_teams.add(line[:-1])

            file.close()

            stage = 8
            file = open("history.txt", "w")

            _stage_play(stage)

            print("\n{} won the competition!!!".format(team_list.pop()))
            file.write("\n{} is the winner!".format(tmp_teams.pop()))
            file.close()

            print("\nDo you want to see the path of a particular team? [Y/N]")
            in_ch = ord(getch())
            while in_ch == 89 or in_ch == 121: # (89 == 'y', 121 == 'Y')
                team_name = input("Enter team's name: ")

                file = open("history.txt", "r")
                tmp_tuple = tuple(file.readlines())
                stg = 8
                key_check = False #for penalties
                for line in tmp_tuple:
                    if key_check == True and "Penalty" in line:
                        print("{}".format(str(line[:-1])))
                        key_check = False
                    else:
                        key_check = False
                    if team_name in str(line):
                        if stg == 1:
                            print("Final: {}".format(str(line[:-1])))
                        elif stg == 0:
                            print(str(line[:-1]))
                        else:
                            print("Stage 1/{}: {}".format(stg, str(line[:-1])))
                        stg //= 2
                        key_check = True
                
                if stg == 8:
                    print("No such team!")
                print("Do you want to see more? [Y/N]")
                in_ch = ord(getch())
                file.close()
            os.system("clear") 

        elif in_ch == 50: # 2) Show all teams (50 == '2')
            os.system("clear") 
            file = open("commands_list.txt", "r")
            for team in file:
                print(team[:-1])
            file.close()

            _return_to_main()
            

        elif in_ch == 51: # 3) Change teams
            os.system("clear") 
            print("Warning: next steps will delete all previous data!\nContinue? [Y/N]")
            in_ch = ord(getch())

            if in_ch == 89 or in_ch == 121: # (89 == 'y', 121 == 'Y')

                os.system("clear") 
                print("Your must enter 16 teams in total:\n")

                file = open("commands_list.txt", "w")
                for team in range(16):
                    print("Enter team #{}: ".format(team + 1))
                    file.write(input())
                    file.write('\n')
                file.close()

                _return_to_main()

            else:
                os.system("clear") 

        elif in_ch == 52: # 4) Exit (52 == '4')
            _exit()

        else:
            os.system("clear")
