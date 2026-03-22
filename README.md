## Woven Monopoly
* This project simulates Woven Monopoly using pre-determined rolls and boards which are loaded in
* It outputs the positions, balances and properties owned of each player after every turn
* It outputs the winner;s name, final positions, balances, and properties owned by all players at the end of the game
*

## Game rules (copied from earlier README)
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)

## Project Structure
core/
   game.py - game logic and turn flow
   player.py - player class
   Spaces.py - board space classes
   jsonLoader.py - loads board data from JSON
data/
   board.json - contains the spaces which will be loaded
   rolls.json - dice rolls
main.py - runs the simulation

## Assumptions
Regarding rent, in the game rules the rent itself isnt specified. I've chosen
to make the rent the same as the price in order to imitate a real game of monopoly where
the rent is roughly proportional to the price, with more expensive properties charging higher rents

## Execution Instructions
From the project root, run the following into the terminal from the project root:

python3 main.py > game_log.txt

*note for windows users this will be:
 python main.py > game_log.txt

 The game results will show up in game_log.txt, where the rolls1 is executed 
 followed by rolls 2

## Design Process
* Broke down the task into the following steps and tested each one
  * creating objects (spaces, players, an instance of the game)
  * reading the files in correctly (Rolls and the board)
  * moving the players and go logic
  * buying logic and property ownership
  * renting and monoply logic 
  * winning detection






## original README 

## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

## Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)


## Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?


The specifics and implementation of this code is completely up to you!

### What we are looking for:
* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code.  You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.
