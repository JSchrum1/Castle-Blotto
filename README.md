# Castle-Blotto
# Create blotto tournaments and view detailed statistics for each player. 
# Play by running play.py or by entering player info into starterPlayers() then running the main class. 
# I prefer using starterPlayers because it saves player info from play to play 

# Blotto Rules 
# 1.) You get 100 troops to put on whatever castles you want 
# 2.) Each Castle is worth it's number of points (castle 4 is worth 4 points, etc.) 
# 3.) Castles are fought starting at castle 1 and go in order 
# 4.) First person to 20 points wins, any castles after someone get to 20 points don't count 
# 5.) Whoever wins the most head to head matches is the overall winner

# I am not currently aware of any bugs, however it is fairly inefficient because each match is played twice
# (once for player 1 vs player 2 and once for player 2 vs player 1)
# All matches are also replayed when printing statistics.

# I initially used lists to store all player info but I then realized I should have used objects so I edited it to start with
# objects. Unfortunately I do not have time to go back and change the rest of the code, so the objects are converted into 
# a list of lists to work with the rest of the code.

# The Castle class handles finding and printing overall results
# The Groups class allows users to give players specific groups so users can run multiple independent tournaments or
#   group them all together but still store all data in the same program
# The head2head class handles most statistics for head to head matches
# The player class handles adding new players and converting these objects into a list. It can also print player info
# The main class allows users to enter players directly into the starterPlayers() function and commands into the main()
#   function to run the program all at once to view results
# The play class allows users to play from the terminal
