"""Test for my functions.
"""

from functions import intro, choose_movie, game_1, game_2, game_3, retry


# for these tests, I know I couldn't really do many tests 
# because there's no parameters or returned outputs

def test_intro():

    assert callable(intro)
    
def test_choose_movie():

    assert callable(choose_movie)
    
    
def test_game_1():

    assert callable(game_1)
    
def test_game_2():

    assert callable(game_2)
    
       
def test_game_3():

    assert callable(game_3)
    
def test_retry():

    assert callable(retry)
