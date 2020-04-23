import random

#wordlist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush', 'south']
wordlist = ['BARDAK']
word = random.choice(wordlist)
wordlist = list(word)
#guess = "p"
display = "-" * len(word)
display = list(display)
joindisplay = "".join(display)
gamecontinue = True
falsecount = 0

print(f"Here is the word: >>> {joindisplay} <<<")
while (gamecontinue):
    guess = input("Give me a letter: ")
    correctanswer = 0
    for x, i in enumerate(wordlist):
        if guess == i:
            display[x] = guess
            correctanswer = 1
    if correctanswer == 1:
        print(f"Correct! Your letter -->{guess} is in the word!")
    if correctanswer == 0:
        falsecount += 1
    if falsecount >= 1:

        print('''     ^_^_^_^_^_^ 
     |   *  *  |
     (    L    )
      \   @  /''')

    if falsecount == 2:
        print('''    |   \ /   |
    |    *    |
    |____*____|
                ''')
    if falsecount == 3:
        print(''' / / |   \ /   |
/ /  |    *    |
     |____*____|

        ''')
    if falsecount == 4:
        print(''' / / |   \ /   | \  
/ /  |    *    |  \ \ 
     |____*____|

                ''')
    if falsecount == 5:
        print(''' / / |   \ /   | \  
/ /  |    *    |  \ \ 
     |____*____|
  |____|     
                    ''')
    if falsecount == 6:
        print(''' / / |   \ /   | \  
/ /  |    *    |  \ \ 
     |____*____|
  |____|     |____| 
                    ''')
    print("Here is the word: >>>","".join(display),"<<<")
    if falsecount == 6:
        print("Game Over! You died :( ")
        gamecontinue = False
    if display == wordlist:
        print("Congratulations! you won the game!!")
        gamecontinue = False




