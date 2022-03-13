
import numpy as np


def intro():
    """This is the beginning of the quiz. You get introduced the game's 
    instructions and input your name to get a greeting back. Then, it 
    goes to the choose_movie function.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
       
    """
    
    # explains the game, allows user to input name and returns greeting 
    name = input("Hi! Welcome to High School Musical Song Trivia!\n"
                 "This quiz will test you on your knowledge of songs from the\n"
                 "movies and see if you're a true fan :)\n"
                 "What's your name?\n")
    print("Great! Nice to have you, {}. Let's go!".format(name))
    
    choose_movie()

    
def choose_movie():
    """This allows the player to choose which movie they want 
    to get tested on. From there, it goes to the game function which
    corresponds to that chosen movie.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
       
    """
    
    # explains background and user can input which movie they want
    # turns input into integer
    chosen_movie = int(input("You might know that there are 3 movies in the\n"
                             "High School Musical franchise. Which movie do you want to\n"
                             "test your song knowledge on?\n"
                             "Enter 1, 2, or 3! \n"))
    
    # for chosen game, returns custom message and opens the game
    if chosen_movie == 1:
        movie_title = "High School Musical"
        print("Great! You've chosen to guess songs from the original " + movie_title + ".")
        game_1()
        
    elif chosen_movie == 2:     
        movie_title = "High School Musical 2"
        print("Great! You've chosen to guess songs from " + movie_title + ".")
        game_2()
        
    elif chosen_movie == 3:     
        movie_title = "High School Musical 3"
        print("Great! You've chosen to guess songs from " + movie_title + ".")
        game_3()
    
    # returns back to start of function if you don't enter existing movie
    else:
        print("Sorry, that doesn't exist! Try entering 1, 2 or 3!")
        choose_movie()

        
## COMMENTS:
# game_1, game_2, and game_3 follow the same format in terms of if/for loops,
# retrieving lyrics, and checking players' answers.
# The only differences are that they open different text files that
# hold lyrics from their own respective movies.
# So, I've only put comments on game_1 so it's not repetitive.


def game_1():
    """Begins the game. Presents the player with a randomly chosen lyric
    from the 1st movie and asks them which song it is from.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
       
    """
    # instructions
    print("Ok! Now, we'll be diving into the first movie!\n"
          "Make sure you check your spelling and punctuation.\n"
          "Here's the lyric!\n")
    
    # opens up the text file which contains the lyrics for the movie
    # cited source: https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
    # this source helped me understand the open and readlines methods; I've modified the source's examples
    # to fit my variables and text files
    with open('my_module/hsm_1_song_lyrics.txt', 'r') as hsm_1_song_lyrics:
        
        # reads over each line in song text file, presents as list in variable 'lines'
        lines = hsm_1_song_lyrics.readlines()
        
        # chooses a random numbered lyric in the file
        rand_line = np.random.choice(len(lines))
        
        # chosen random lyric, removes white space around it
        lyric = lines[rand_line].strip()
        
        # turns input into all lower case as answer
        answer = input("[" + lyric + ".]" +
                       " What song is this from?\n").lower()

    
        # the range of lines for the entire text file
        my_range = range(0, len(lines))
        
        # library of song titles and their respective lyrics
        hsm_1_songs = {"bop to the top" : my_range[0:44],
                       "breaking free" : my_range[44:113],
                       "getcha head in the game" : my_range[113:160],
                       "start of something new" : my_range[160:210],
                       "stick to the status quo" : my_range[210:314],
                       "we're all in this together" : my_range[314:402],
                       "what i've been looking for" : my_range[402:432],
                       "when there was you and me" : my_range[432:472]}
       
    
    # compares answer to each key (title) and value (lyrics range) in each pair in hsm_1_songs
    for title, lyrics_range in hsm_1_songs.items():
            
        # stores the number of the line position of the randomly chosen lyric
        line_number = int(rand_line)
            
        # checks if the player's answer matches the correct title
        # of the range of lyrics of that song
        if line_number in hsm_1_songs[title]:
                
            # answer is correct, opens replay function
            if answer == title: 
           
                print("Good job! You have a great memory! You must\n"
                          "be a true fan!\n")
                retry()
   
                    
            # answer is wrong, tells player the correct answer and player can replay or end game
            else:
                print("Not quite! This lyric comes from the song, "
                           + "'" + title + "'.") 
                retry()


                        


def game_2():
    """Begins the game. Presents the player with a randomly chosen lyric from 
    the 2nd movie and asks them which song it comes from.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none  
    
    """
    
    print("Ok! Now, we'll be diving into the 2nd movie!\n"
          "Make sure you check your spelling and punctuation.\n")
    
    with open('my_module/hsm_2_song_lyrics.txt', 'r') as hsm_2_song_lyrics:
        
        lines = hsm_2_song_lyrics.readlines()
        
        rand_line = np.random.choice(len(lines))
                
        lyric = lines[rand_line].strip()
        
        my_range = range(0, len(lines))
    
        
        hsm_2_songs = {"what time is it": my_range[0:78],
                       "fabulous" : my_range[78:132],
                       "work this out" : my_range[132:191],
                       "you are the music in me" : my_range[191:244],
                       "i don't dance" : my_range[244:350],
                       "gotta go my own way" : my_range[350:398],
                       "bet on it" : my_range[398:449],
                       "everyday" : my_range[449:502],
                       "all for one" : my_range[502:582]}
        
        
        answer = input("[" + lyric + ".]" +
                       " What song is this from?\n").lower()
        
        
        for title, lyrics_range in hsm_2_songs.items():
            
            line_number = int(rand_line)

            if line_number in hsm_2_songs[title]:
                
                if answer == title: 
           
                    print("Good job! You have a great memory! You must\n"
                          "be a true fan!\n")
                    retry()

                else:
                    print("Not quite! This lyric comes from the song, "
                           + "'" + title + "'.")
                    retry()

                    
def game_3():
    """Begins the game. Presents the player with a randomly chosen lyric from 
    the 3rd movie and asks them which song it comes from.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
       
    """
    
    movie = 3
    print("Ok! Now, we'll be diving into the 3rd movie!\n"
          "Make sure you check your spelling and punctuation.\n")
    
    with open('my_module/hsm_3_song_lyrics.txt', 'r') as hsm_3_song_lyrics:
        
        lines = hsm_3_song_lyrics.readlines()
        
        rand_line = np.random.choice(len(lines))
                
        lyric = lines[rand_line].strip()
        
        my_range = range(0, len(lines))
    
        
        hsm_3_songs = {"now or never": my_range[0:117],
                       "right here right now" : my_range[117:163],
                       "i want it all" : my_range[163:278],
                       "can i have this dance" : my_range[278:321],
                       "a night to remember" : my_range[321:432],
                       "just wanna be with you" : my_range[432:461],
                       "the boys are back" : my_range[461:507],
                       "walk away" : my_range[507:543],
                       "scream" : my_range[543:607],
                       "high school musical" : my_range[607:678]}
        

        answer = input("[" + lyric + ".]" +
                       " What song is this from?\n").lower()
        
        
        for title, lyrics_range in hsm_3_songs.items():
            
            line_number = int(rand_line)

            if line_number in hsm_3_songs[title]:
                
                if answer == title: 
           
                    print("Good job! You have a great memory! You must\n"
                          "be a true fan!\n")
                    retry()
                
                else:
                    print("Not quite! This lyric comes from the song, "
                           + "'" + title + "'.")
                     
                    retry()

                    
def retry():
    """Asks if player would like to retry the game.
    If answered yes, returns to choose_movie function.
    If answer no, ends game with a message.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    bye = string
        A goodbye message to the player.
       
    """
    
    retry = input("Would you like to try this quiz again?\n"
                  "You can switch up the movie or test yourself again!\n"
                  "Answer 'yes' or 'no'.\n")
                            
    if retry == 'yes':
        choose_movie()
                    
    else:
        print("Thanks for playing! I hope you had fun!")
