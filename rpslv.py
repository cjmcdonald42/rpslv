#
#           project:    rpslv.py
#            author:    Charles J McDonald <cmcdonald@woonsocketschools.com>
#           version:    2024.10.10.01
#
#   description: Rock, Paper, Scissors, Lizard, Spock for 1 or 2 players
#
import random

# === Introduce the Game
# Rules = Rock, Paper, Scissors, Lizard, Spock
print("""
=== RPS Duel === \n
    Challengers, step forward and prepare thyselves for an epic duel!!!
""")

# === Get the names of our challengers
player1 = input("First Challenger, what is thy name? : ")
player2 = input("Second Challenger, state thy name or enter 'C' to practice against the computer: ")
weaponsFullName = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
computerPlayer = "Horatio the Chaotic Computer"
weapons = ["R", "P", "S", "L", "V"]
score1 = score2 = 0
bet1 = bet2 = 0
wallet1 = wallet2 = 20      # Starting amount of currency
isPlaying = True

while isPlaying:
    # === Choose your move
    print("""
    On yon table before thee reste weapons five:
        [R]ock : An ancient weapon of destruction
        [P]aper: An elegant weapon for the literate
        [S]cissors: A brutish blade for the stylish
        [L]izard: A deadly reptile from the far realms
        [V]Spock: A being of ineffable logic
    """)
    bet1 = int(input(f"{player1}, you currently have {wallet1} peri in thy wallet. Pray-tell, What wouldst thou wager? : "))
    wallet1 -= bet1
    weapon1 = input(f"{player1}, choose thy weapon! : ")
    if player2 == "C":  # Computer randomly chooses a weapon
        randomWeapon = random.randint(0, 4)
        weapon2 = weapons[randomWeapon]
        bet2 = 2 + random.randint(0,4)
        wallet2 -= bet2
        print(f"Horatio the Chaotic Computer chooses {weaponsFullName[randomWeapon]} and wagers {bet2} peri.")
    else:
        bet2 = int(input(f"{player2}, you currently have {wallet2} peri in thy wallet. Pray-tell, What wouldst thou wager? : "))
        wallet2 -= bet2
        weapon2 = input(f"{player2}, choose thy weapon! : ")

    # === Resolve combat
    if weapon1 == weapon2:      # -- A Draw
        print("Thou hast ended in a Draw!")
        wallet1 += bet1
        wallet2 += bet2
    elif weapon1 == "R":  # Player1 chooses Rock
        if weapon2 == "P":
            print(f"Paper covers Rock! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        elif weapon2 == "V":
            print(f"Spock vapourizes Rock with his phaser! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        elif weapon2 == "L":
            print(f"Rock crushes Lizard! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        else:  # weapon2 must be Scissors
            print(f"Rock crushes Scissors! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2

    elif weapon1 == "P":  # Player1 chooses Paper
        if weapon2 == "R":
            print(f"Paper covers Rock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "V":
            print(f"Paper disprooves Spock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "L":
            print(f"Lizard shreds Paper! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Scissors cut Paper! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    elif weapon1 == "L":  # Player1 chooses Lizard
        if weapon2 == "V":
            print(f"Lizard poisons Spock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "P":
            print(f"Lizard eats Paper! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "R":
            print(f"Rock crushes Lizard! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Scissors decapitate Lizard! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    elif weapon1 == "V":  # Player1 chooses Spock
        if weapon2 == "S":
            print(f"Spock smashes Scissors! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "R":
            print(f"Spock vapourizes Rock with his phaser! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "L":
            print(f"Lizard poisons Spock! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Paper disproves Spock! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    else:  # weapon1 must be Scissors
        if weapon2 == "L":
            print(f"Scissors decapitate Lizard! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "P":
            print(f"Scissors cut Paper! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "V":
            print(f"Spock smashes Scissors! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Rock breaks Scissors! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    print(f"{player1} hath scored {score1} points and has {wallet1} peri in his purse.")
    if player2 == "C":
        print(f"{computerPlayer} hath scored {score2} points and has {wallet1} peri in his purse.")
    else :
        print(f"{player2} hath scored {score2} points and has {wallet1} peri in his purse.")

    # == Play again?
    ask = input("Would thoust like another round? : ")
    if ask != "Y" :
        isPlaying = False

if score1 > score2:
    print(f"{player1} win-ith the duel with {score1} points!")
elif score2 > score1:
    if player2 == "C": player2 = computerPlayer
    print(f"{player2} win-ith the duel with {score2} points!")
else:
    print("The duel doth end in a draw!")
