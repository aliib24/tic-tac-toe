from ast import While
from cProfile import label
import random
from tracemalloc import start
from numpy import intp
from scipy import rand
from termcolor import colored
import tkinter
from tkinter import messagebox
import time


game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

# for co-op playing


def check_player_1():
    if game[0][0] == "x" and game[0][1] == "x" and game[0][2] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    elif game[1][0] == "x" and game[1][1] == "x" and game[1][2] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    elif game[2][0] == "x" and game[2][1] == "x" and game[2][2] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")

    elif game[0][0] == "x" and game[1][1] == "x" and game[2][2] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    elif game[0][2] == "x" and game[1][1] == "x" and game[2][0] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")

    elif game[0][0] == "x" and game[1][0] == "x" and game[2][0] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    elif game[0][1] == "x" and game[1][1] == "x" and game[2][1] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    elif game[0][2] == "x" and game[1][2] == "x" and game[2][2] == "x":
        print(colored("Player 1 wins", 'red'))
        messagebox.showinfo("the winner", "player 1 wins")
    else:
        print("Draw, play better next time")


def check_player_2():
    if game[0][0] == "o" and game[0][1] == "o" and game[0][2] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    elif game[1][0] == "o" and game[1][1] == "o" and game[1][2] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    elif game[2][0] == "o" and game[2][1] == "o" and game[2][2] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")

    elif game[0][0] == "o" and game[1][1] == "o" and game[2][2] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    elif game[0][2] == "o" and game[1][1] == "o" and game[2][0] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")

    elif game[0][0] == "o" and game[1][0] == "o" and game[2][0] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    elif game[0][1] == "o" and game[1][1] == "o" and game[2][1] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    elif game[0][2] == "o" and game[1][2] == "o" and game[2][2] == "o":
        print(colored("Player 2 wins", 'red'))
        messagebox.showinfo("the winner", "player 2 wins")
    else:
        print("Draw, play better next time")


# CPU
def check_cpu():
    if game[0][0] == "o" and game[0][1] == "o" and game[0][2] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    elif game[1][0] == "o" and game[1][1] == "o" and game[1][2] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    elif game[2][0] == "o" and game[2][1] == "o" and game[2][2] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")

    elif game[0][0] == "o" and game[1][1] == "o" and game[2][2] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    elif game[0][2] == "o" and game[1][1] == "o" and game[2][0] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")

    elif game[0][0] == "o" and game[1][0] == "o" and game[2][0] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    elif game[0][1] == "o" and game[1][1] == "o" and game[2][1] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    elif game[0][2] == "o" and game[1][2] == "o" and game[2][2] == "o":
        print(colored("CPU wins", 'red'))
        messagebox.showinfo("the winner", "CPU wins")
    else:
        print("Draw, play better next time")


###############################################################################################
#                                       #############                                         #
#                                       # MAIN CODE #                                         #
#                                       #############                                         #                                                                             #
###############################################################################################


#################################################--single player--###################################################
print(colored("select the mode: \n single player: 1 \n multiplayer:2  \n", "green"))
mode = input()

if mode == '1':
    print(colored("singple player mode", "red"))
    while True:
        # First Player
        print("Player 1")
        while True:
            row = int(input())
            col = int(input())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "x"
                    break
                else:
                    print("Try Again")
            else:
                print("Keep Focus")
        check_player_1()
        for row in game:
            print(colored(row, 'green'))

        end = time.time()
        game_time = end-start
        print("Total Game time is: ", game_time)

        # second player
        print("CPU")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "o"
                    break
        check_cpu()
        for row in game:
            print(colored(row, 'yellow'))

        end = time.time()
        game_time = end-start
        print("Total Game time is: ", game_time)

#################################################--multiplayer--###################################################

elif mode == '2':
    print(colored("multiplayer mode", "red"))
    while True:
        # First Player
        print("Player 1")
        while True:
            row = int(input())
            col = int(input())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "x"
                    break
                else:
                    print("Try Again")
            else:
                print("Keep Focus")
        check_player_1()
        for row in game:
            print(colored(row, 'green'))

        # second player
        print("Player 2")
        while True:
            row = int(input())
            col = int(input())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "o"
                    break
                else:
                    print("Try Again")
            else:
                print("Keep Focus")
        check_player_2()
        for row in game:
            print(colored(row, 'yellow'))
        end = time.time()
        game_time = end-start
        print("Total Game time is: ", game_time)
