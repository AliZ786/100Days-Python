def treasure_island_game():
    print(""" / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/ """)

    print("\n********** Welcome to Treasure Island! **********")

    choice_message = "\nPlease enter your choice: "
    end = "\n********* GAME OVER *********"
    win = "\n******** YOU WIN ********"

    while True:
        print("\nYou\'re at a crossroad, would you like to the left path or the right path? Press 'l' for left and 'r' for right")
        choice1 = input(choice_message).lower()

        if choice1 == "l":
            print("\nYou have chosen to go left. You have found a lake, would you like to cross to swim to the other side, or wait for someone to rescue you? Press 's' to swim or 'w' to wait")
            choice2 = input(choice_message).lower()

            if choice2 == "s":
                print("You have chosen to swim to the other side. On the other side, you come face to face with a huge castle with three different color doors. Once again, you must make an important decision, would you choose the blue door (press 'b'), the red door (press 'r'), or the yellow door (press 'y')")
                choice3 = input(choice_message).lower()

                if choice3 == "y":
                    print("After following the yellow door, and a long struggle through the castle stairs, you finally reach the throne room. The King instantly notices you, and commends you for bravery, and says that any of the treasure that he has would be available to you. Seems like you really hit the jackpot!")
                    print(win)

                elif choice3 == "b":
                    print("You have chosen to follow the blue door. You see a big door, however, just as you are about to enter the door, the sweet aroma of food hits your nose just right, and you decide to follow it. Your nose leads to room to the kitchen, where gargoyles, orcs, werewolves, all the foul beasts you can imagine are cooking up their meals. Guess human is now on the menu.")
                    print(end)

                else:
                    print("You have chosen to follow the red door. You keep on traversing the room, but suddenly realize that it's getting warmer and warmer. Thinking that there may be some smelting area where they have rare minerals and ore, you press on. You reach the end of the room to find out the room is just fire everywhere. You do not know what to do, until all of sudden (and I don't know why) you think this must all be a dream and jump into the fire. Guess it's true what they said, you never were really bright.")
                    print(end)

            else:
                print("You have chosen to wait it out. Days have gone by and you have had nothing to eat, you start to get hungry. Suddenly, you see a deer, and go to chase it for food. You chase it for a long time in the forest, hoping to finally quench your hunger. Unbeknownst to you, you have stepped foot in the Lion's Den. Guess the predator has become the prey.")
                print(end)

        else:
            print("You have chosen to go right. You have found a big tree, you see something shiny on the top. In your attempt to climb the tree to retrieve this shiny object, the tree branch snaps and you fall into the abyss. Rule 101 kid, if something looks shiny from far away, IT'S A TRAP.")
            print(end)

        play_again = input("\nDo you want to play again? (Press 'y' for yes, any other key to exit): ").lower()
        if play_again != 'y':
            print("Thank you for playing Treasure Island!")
            break

# Call the function to start the game
treasure_island_game()
