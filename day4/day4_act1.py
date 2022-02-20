# DAY 4 - ACTIVITY 1
# Program Description: This is a program that uses a single while loop to
# print out 50 messages. 49 of the messages are numbered 1-49 while the
# last one informs the user that the loop has ended.

# Here, a while-else was used to print out the desired messages.
i = 0
while i < 49:
    i += 1
    print ( " Python while loop number {}.".format( i ) )
else:
    print ( " END OF THE LOOP. " )
