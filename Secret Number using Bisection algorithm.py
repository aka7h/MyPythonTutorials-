print("Please think of a number between 0 and 100!")
lo = 0
hi = 100
ans = (hi+lo)/2
while True:
    print("Is your secret number %s?" % ans)
    r = raw_input('''Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ''')
    if(r == 'h'):
        hi = ans
    elif(r == 'l'):
        lo = ans
    elif(r == 'c'):
        print("Game Over. Your secret number was %s" % ans)
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = (hi + lo)/2    