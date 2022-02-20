
# Day2 - Activity2
# Song Title: She’s Kinda Hot by 5 Seconds of Summer
# Program Description: This is a program that uses the user's input to replace the first 3 nouns and 3 adjectives in the song lyrics.

# The lyrics of the song that was taken from google search
originalLyrics = """My girlfriend's bitchin' 'cause I always sleep in \n
 She's always screamin' when she's callin' her friend \n
 She's kinda hot though \n
 Yeah, she's kinda hot though \n
 (Just an itty bitty, little bit hot)"""

# The three nouns and 3 adjectives were replaced with {}. This is so it can be accommodated by the format() method.
editedLyrics = """My {}'s {}' 'cause I always sleep in \n
 She's always screamin' when she's callin' her {} \n
 She's kinda {} though \n
 Yeah, she's kinda {} though \n
 (Just an {} bitty, little bit hot)"""

# The program will run continously as long as the user hasn't closed it.
while True:
    print ( "-------------------- ENTER DETAILS --------------------" )
    firstNoun = str ( input ( " Enter the first noun: " ) )
    secondNoun = str ( input ( " Enter the second noun: ") )
    thirdNoun = str ( input ( " Enter the third noun: " ) )
    print ( "-------------------------------------------------------" )
    firstAdj = str ( input ( " Enter first Adjective: " ) )
    secondAdj = str ( input ( " Enter second Adjective: " ) )
    thirdAdj = str ( input ( " Enter third Adjective: " ) )
    print ( "-------------------------------------------------------\n" )
    print ( "======================= RESULT ========================" )
    print ( " Original Song Lyrics: \n" , originalLyrics )
    print ( "=======================================================" )
    # The edited lyrics undergoes the format method where the user's input are injected into their respective place in the lyrics.
    # Moreover, the uppercase function was used to highlight the replaced nouns and adjectives.
    replacedLyrics = editedLyrics.format( firstNoun.upper(), secondNoun.upper(), thirdNoun.upper(), firstAdj.upper(), secondAdj.upper(), thirdAdj.upper() )
    print ( " Replaced Song Lyrics: \n" , replacedLyrics )
    print ( "=======================================================\n" )
    
    
