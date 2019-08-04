def hangman(word):
	wrong=0
	import random
	wordlist=["cat",
                  "dog",
                  "pig",
                  "lion",
                  "tiger",
                  "duck",
                  "chicken",
                  "monkey"]
	word=random.choice(wordlist)    '''select one word form word list, e.g. chicken'''
	stages=["",
	       "______      ",
	       "|           ",
	       "|     |     ",
	       "|     0     ",
	       "|    /|\    ",
	       "|    / \    ",
	       "|           ",
	       ]
	rletters=list(word)             '''chicken->["c","h","i","k","e","n"]'''
	board=["_"]*len(word)           '''["_","_","_","_","_","_"]'''
	win=False
	print("Welcome to Hangman")
	while wrong<len(stages)-1:      
            print("\n")
            msg="Guess a letter"        '''c'''
            char=input(msg)
            if char in rletters:
                cind=rletters.index(char)   '''cind=1'''
                board[cind]=char            '''["c","_","_","_","_","_"]'''
                rletters[cind]='$'          '''["$","h","i","k","e","n"]'''
            else:
                wrong +=1
            print(("".join(board)))         '''print scords'''
            e=wrong+1
            print("\n".join(stages[0:e]))   '''print hangman'''
            if "_" not in board:
                print("You win!")
                print("".join(board))       '''print chicken'''
                win=True
                break
        if not win:
            print("\n".join(stages[0:wrong]))           '''print whole hangman'''
            print("You lose! It was {}.".format(word))  '''print "You lose! It was chicken."'''

hangman(word)
