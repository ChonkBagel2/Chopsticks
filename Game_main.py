import os, time


class Hands():

    max_fingers = 4


    def __init__(self,left_fingers,right_fingers):
        self.left_fingers = left_fingers
        self.right_fingers = right_fingers


    def display_left(self):
        print(f"The current amount of left fingers are {self.left_fingers}")


    def display_right(self):
        print(f"The current amount of right fingers are {self.right_fingers}")


    def add_to_left(self, value):
        max_add_value = self.max_fingers - self.left_fingers
        
        if value > max_add_value:
            self.left_fingers = 0

        elif value <= max_add_value and self.left_fingers > 0:
            self.left_fingers += value
        
        else:
            print("invalid")

    
    def add_to_right(self, value):
        max_add_value = self.max_fingers - self.right_fingers

        if value > max_add_value:
            self.right_fingers = 0

        elif value <= max_add_value and self.right_fingers > 0:
            self.right_fingers += value
        
        else:
            print("invalid")


#hand1 = Hands(1,1)
#hand1.add_to_left(3)
#hand1.display_left()

class Players(Hands):


    def attack_left_from_left(self, d_player_obj):
        if self.left_fingers > 0 and d_player_obj.left_fingers > 0:
            d_player_obj.add_to_left(self.left_fingers)
            return True

        else:
            return False

    
    def attack_left_from_right(self, d_player_obj):
        if self.right_fingers > 0 and d_player_obj.left_fingers > 0:
            d_player_obj.add_to_left(self.right_fingers)
            return True

        else:
            return False


    def attack_right_from_left(self, d_player_obj):
        if self.left_fingers > 0 and d_player_obj.right_fingers > 0:
            d_player_obj.add_to_right(self.left_fingers)
            return True

        else:
            return False


    def attack_right_from_right(self, d_player_obj):
        if self.right_fingers > 0 and d_player_obj.right_fingers > 0:
            d_player_obj.add_to_right(self.right_fingers)
            return True

        else:
            return False


    def check_attack_left_from_left(self, d_player_obj):
        if self.left_fingers > 0 and d_player_obj.left_fingers > 0:
            #d_player_obj.add_to_left(self.left_fingers)
            return True

        else:
            return False

    
    def check_attack_left_from_right(self, d_player_obj):
        if self.right_fingers > 0 and d_player_obj.left_fingers > 0:
            #d_player_obj.add_to_left(self.right_fingers)
            return True

        else:
            return False


    def check_attack_right_from_left(self, d_player_obj):
        if self.left_fingers > 0 and d_player_obj.right_fingers > 0:
            #d_player_obj.add_to_right(self.left_fingers)
            return True

        else:
            return False


    def check_attack_right_from_right(self, d_player_obj):
        if self.right_fingers > 0 and d_player_obj.right_fingers > 0:
            #d_player_obj.add_to_right(self.right_fingers)
            return True

        else:
            return False

        
    def split_even(self):
        if self.right_fingers == 0:
            if self.left_fingers == 2 or self.left_fingers == 4:
                x = self.left_fingers / 2
                self.left_fingers = int(x)
                self.right_fingers = int(x)
                return True
            
            else:
                return False

        elif self.left_fingers == 0:
            if self.right_fingers == 2 or self.right_fingers == 4:
                x = self.right_fingers / 2
                self.right_fingers = int(x)
                self.left_fingers = int(x)
                return True
            
            else:
                return False

        else:
            return False


    def split_2(self, strng):
        if strng == 'sp12':
            if self.left_fingers == 0 and self.right_fingers == 3:
                self.left_fingers = 1
                self.right_fingers = 2
                
                return True

            elif self.left_fingers == 3 and self.right_fingers == 0:
                self.left_fingers = 1
                self.right_fingers = 2
                
                return True

            else:
                return False

        elif strng == 'sp21':
            if self.left_fingers == 0 and self.right_fingers == 3:
                self.left_fingers = 2
                self.right_fingers = 1
                
                return True

            elif self.left_fingers == 3 and self.right_fingers == 0:
                self.left_fingers = 2
                self.right_fingers = 1
                
                return True

            else:
                return False

        elif strng == 'sp13':
            if self.left_fingers == 0 and self.right_fingers == 4:
                self.left_fingers = 1
                self.right_fingers = 3
                
                return True

            elif self.left_fingers == 4 and self.right_fingers == 0:
                self.left_fingers = 1
                self.right_fingers = 3
                
                return True

            else:
                return False

        elif strng == 'sp31':
            if self.left_fingers == 0 and self.right_fingers == 4:
                self.left_fingers = 3
                self.right_fingers = 1
                
                return True

            elif self.left_fingers == 4 and self.right_fingers == 0:
                self.left_fingers = 3
                self.right_fingers = 1
                
                return True

            else:
                return False

        else:
            return False


    def check_split_even(self):
        if self.right_fingers == 0:
            if self.left_fingers == 2 or self.left_fingers == 4:
                return True
            
            else:
                return False

        elif self.left_fingers == 0:
            if self.right_fingers == 2 or self.right_fingers == 4:
                return True
            
            else:
                return False

        else:
            return False


    def check_split_2(self, strng):
        if strng == 'sp12':
            if self.left_fingers == 0 and self.right_fingers == 3:
                
                return True

            elif self.left_fingers == 3 and self.right_fingers == 0:
                
                return True

            else:
                return False

        elif strng == 'sp21':
            if self.left_fingers == 0 and self.right_fingers == 3:
                
                return True

            elif self.left_fingers == 3 and self.right_fingers == 0:
                
                return True

            else:
                return False

        elif strng == 'sp13':
            if self.left_fingers == 0 and self.right_fingers == 4:
                
                return True

            elif self.left_fingers == 4 and self.right_fingers == 0:
                
                return True

            else:
                return False

        elif strng == 'sp31':
            if self.left_fingers == 0 and self.right_fingers == 4:
                
                return True

            elif self.left_fingers == 4 and self.right_fingers == 0:
                
                return True

            else:
                return False

        else:
            return False

        
    def check_hand(self):
        if self.left_fingers == 0 and self.right_fingers == 0:
            return True
        else:
            return False



class Game(Players):
    
    #Human = [p1.left_fingers, p1.right_fingers]
    #Comp = [p2.left_fingers, p2.right_fingers]


    def __init__(self):
        self.p1 = Players(1,1)
        self.p2 = Players(1,1)

    
    def change_turn(self, turn):
        if turn == "human":
            turn = "comp"
        else:
            turn = "human"
        
        return turn


    def first_turn(self):
        fturn = 'abc'
        valid_options = ['y', 'n']
        while fturn not in valid_options:
            fturn = input("\n" + "Do you wanna go first? y/n \n").lower()

        if fturn == "y":
            turn = "human"
        else:
            turn = "comp"
        
        return turn


    def display_board(self, turn):
        os.system('cls')
        print(f"Comp's hand \t \t Current Turn: {turn.capitalize()} \n")
        print([self.p2.left_fingers, self.p2.right_fingers])
        print("\n \nHuman's hand \n")
        print([self.p1.left_fingers, self.p1.right_fingers])
        print("\n")

    
    def show_move(self, turn, move):
        if turn == "human":
            print('\n')
            print(f'You chose: {move}')
            time.sleep(2)

        else:
            print('\n')
            print(f'Comp chose: {move}')
            time.sleep(4)


    def play_game(self, turn, command):
        if turn == "human":
            player_obj = self.p1
            player_obj2 = self.p2
        else:
            player_obj = self.p2
            player_obj2 = self.p1

        if command == 'lfl':
            move = player_obj.attack_left_from_left(player_obj2)
            return move
        
        elif command == 'lfr':
            move = player_obj.attack_left_from_right(player_obj2)
            return move
        
        elif command == 'rfl':
            move = player_obj.attack_right_from_left(player_obj2)
            return move

        elif command == 'rfr':
            move = player_obj.attack_right_from_right(player_obj2)
            return move

        elif command == 'sp even':
            move = player_obj.split_even()
            return move
        
        elif command in ['sp12', 'sp21', 'sp13', 'sp31']:
            move = player_obj.split_2(str(command))
            return move


    def check_play(self, turn, command):
        if turn == "human":
            player_obj = self.p1
            player_obj2 = self.p2
        else:
            player_obj = self.p2
            player_obj2 = self.p1

        if command == 'lfl':
            move = player_obj.check_attack_left_from_left(player_obj2)
            return move
        
        elif command == 'lfr':
            move = player_obj.check_attack_left_from_right(player_obj2)
            return move
        
        elif command == 'rfl':
            move = player_obj.check_attack_right_from_left(player_obj2)
            return move

        elif command == 'rfr':
            move = player_obj.check_attack_right_from_right(player_obj2)
            return move

        elif command == 'sp even':
            move = player_obj.check_split_even()
            return move
        
        elif command in ['sp12', 'sp21', 'sp13', 'sp31']:
            move = player_obj.check_split_2(str(command))
            return move


    #I might have to do this, okay I have to , okay i have done some things
    def simulate_play(self, command, attack_player_object, defense_player_object):

        if command == 'lfl':
            move = attack_player_object.attack_left_from_left(defense_player_object)
            return move
        
        elif command == 'lfr':
            move = attack_player_object.attack_left_from_right(defense_player_object)
            return move
        
        elif command == 'rfl':
            move = attack_player_object.attack_right_from_left(defense_player_object)
            return move

        elif command == 'rfr':
            move = attack_player_object.attack_right_from_right(defense_player_object)
            return move

        elif command == 'sp even':
            move = attack_player_object.split_even()
            return move
        
        elif command in ['sp12', 'sp21', 'sp13', 'sp31']:
            move = attack_player_object.split_2(str(command))
            return move


    def all_valid_moves(self, turn):

        the_options = ['lfl', 'lfr', 'rfl', 'rfr', 'sp even', 'sp12', 'sp21', 'sp13', 'sp31']

        valid_list = []
        for option in the_options:

            valid = self.check_play(turn, option)

            if valid:
                valid_list.append(option)

        return valid_list


    def check_lose(self):
        result_human = self.p1.check_hand()
        result_comp = self.p2.check_hand()

        if result_human == True or result_comp == True:
            return True
        else:
            return False


    def evaluate(self, player_object):
        score = 0
        
        score += player_object.left_fingers
        score += player_object.right_fingers
        
        if player_object.left_fingers > 0 and player_object.right_fingers > 0:
            score += 1
        
        if player_object.left_fingers + player_object.right_fingers > 4:
            score += 1

        elif player_object.left_fingers == 0 and player_object.right_fingers == 0:
            score = 0

        return score


    def return_state(self, turn):

        if turn == "human":
            attack_player_object = Players(self.p1.left_fingers, self.p1.right_fingers)
            defense_player_object = Players( self.p2.left_fingers, self.p2.right_fingers)

        else:
            attack_player_object = Players(self.p2.left_fingers, self.p2.right_fingers)
            defense_player_object = Players( self.p1.left_fingers, self.p1.right_fingers)

        
        return attack_player_object, defense_player_object


    def simulate(self, valid_move,  attack_player_object, defense_player_object):

        attacker = Players(attack_player_object.left_fingers, attack_player_object.right_fingers)
        defender = Players(defense_player_object.left_fingers, defense_player_object.right_fingers) 

        simulated_state = self.simulate_play(command = valid_move, attack_player_object = attacker, defense_player_object = defender)

        return attacker, defender


    def minimax2(self, turn, valid_moves_list):
        
        current_attacker_state, current_defender_state = self.return_state(turn)
        
        score_list = []
        for moves in valid_moves_list:

            simulated_attacker_state, simulated_defender_state = self.simulate(moves, current_attacker_state, current_defender_state)
            score = self.evaluate(simulated_defender_state)
            score_list.append(score)

        min_index = score_list.index(min(score_list))

        return valid_moves_list[min_index]

#To do's
#Merge Play and Play4 - Done
#Delete Play()              rip The OG play - Done
#Change the names of other plays - Done
#Update the last turn - Done
#Display board's formatiing better - Done
#General formatting
#sub-
#make comp choose random between the first 4


game_on = True
Gameshesh1 = Game()


first_turn = Gameshesh1.first_turn()
if first_turn == "human":
    current_turn = first_turn
    while game_on:
        Gameshesh1.display_board(current_turn)
        
        valid_moves_list = Gameshesh1.all_valid_moves(current_turn)

        if current_turn == "human":
            print("Your valid options are-", ' '.join(valid_moves_list) )
            chosen_move = 'abc'
            while chosen_move not in valid_moves_list:
                chosen_move = input("What do you want to do? \n").lower()

            Gameshesh1.show_move(current_turn, chosen_move)
            valid_move = Gameshesh1.play_game(current_turn, chosen_move)
        
        else:
            comp_move = Gameshesh1.minimax2(current_turn, valid_moves_list)
            Gameshesh1.show_move(current_turn, comp_move)
            valid_move = Gameshesh1.play_game(current_turn, comp_move)
        
        if valid_move:
            game_on = not Gameshesh1.check_lose()
            if not game_on:
                Gameshesh1.display_board(current_turn)
                print(f"{current_turn.capitalize()} wins, better luck next time.")
                time.sleep(2)

            current_turn = Gameshesh1.change_turn(current_turn)

        else:
            print("Not a valid move, try again")
            continue

elif first_turn == "comp":
    current_turn = first_turn
    while game_on:                                                                          
        
        Gameshesh1.display_board(current_turn)
        valid_moves_list = Gameshesh1.all_valid_moves(current_turn)

        if current_turn == "comp":
            comp_move = Gameshesh1.minimax2(current_turn, valid_moves_list)
            Gameshesh1.show_move(current_turn, comp_move)
            valid_move = Gameshesh1.play_game(current_turn, comp_move)
        
        else:
            print("Your valid options are-", " ".join(valid_moves_list) )
            chosen_move = 'abc'
            while chosen_move not in valid_moves_list:
                chosen_move = input('What do you want to do? \n').lower()

            Gameshesh1.show_move(current_turn, chosen_move)
            valid_move = Gameshesh1.play_game(current_turn, chosen_move)

        if valid_move:
            current_turn = Gameshesh1.change_turn(current_turn)
            game_on = not Gameshesh1.check_lose()
            if not game_on:
                current_turn = Gameshesh1.change_turn(current_turn)
                Gameshesh1.display_board(current_turn)
                print(f"{current_turn.capitalize()} wins, better luck next time.")
                time.sleep(2)

        else:
            print("Not a valid move, try again")
            continue



