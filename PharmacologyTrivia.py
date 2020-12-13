### PHARMACOLOGY 101 TRIVIA GAME ###

## QUESTIONS (this is the list of questions separated by category (i.e. Diabetes)
# questions = [question1, question2, question3, question4, question5, question6, question7, question8]

questions = [ 
    ## 1 - CARDIAC DRUGS QUESTIONS ##
    ["What drug class is nitroglycerin in?\n" ,
    "Dopamine is also known by what name?\n" ,
    "True or False: Tachycardia is not an adverse reaction to norepinephrine.\n" ,
    "Lidocaine is considered to be in what drug class?\n" ,
    "This opioid analgesic's contraindications include head injury, respiratory depression, and hypersentivity to opiates. Indications for this drug are pain control and sedation for invasive airway procedures.\n" , 
    "True of False: Diabetic coma is one of the contraindications for magnesium sulfate.\n" , 
    "Levophed is another name for what drug?\n" , 
    "Xylocaine is another name for what local anesthic?\n" , 
    "Also known as adrenaline, this sympathomimetic is :\n" , 
    "This drug is a sympathomimetic, indications include severe cardiogenic shock, and some adverse reactions are headache, angina pectoris, and reflex bradycardia. What drug am I? \n"],

    ## 2 - RESPIRATORY DRUGS QUESTIONS ## 
    ["What medication is used to prevent asthama attacks in patients with bronchial asthma?\n" , 
    "True or Fasle: Tiotropium (spiriva) and Ipatropium ( Artovent) are not indicated for acute asthma attacks?\n" , 
    "Yes or No: Is Antihistamine a type of Bronchodilator\n" , 
    "Which of the following drugs block Acetylcholine in order to prevent bronchoconstriction?\n", 
    "What drug is a respiratory stimulant\n", 
    "What drug supresses the cough reflex in the brain\n", 
    "What is important to note when using Naloxone as a respiratory stimulant?\n", 
    "Which of the following drugs stimulates Beta-2 receptors causing bronchodilation?\n"],

    ## 3 - NEURO DRUGS QUESTIONS ##
    ["What is a common side effect of Carbidopa-levodopa (Sinemet)?\n" , 
    " _______ is used to treat seizures and nerve pain such as trigeminal neuralgia and diabetic neuropathy?\n" , 
    "What is the therapeutic serum range of phenobarbital?\n" , 
    "What s a side effect of Codeine sulfate?\n" , 
    "Drinking __________ can decrease the side effects of Diazepam(Valium)?\n" , 
    "What drug class is Codeine sulfate in?\n" , 
    "________ is a central nervous system stimulant?\n" , 
    "A patient should avoid excessive intake of foods rich in what when taking levodopa?\n" , 
    "The therapeutic level of phenytoin is between what range?\n" , 
    "Which group of drugs mimics parasympathetic activity?\n"],

    ## 4 - DIABETES DRUGS QUESTIONS ## 
    ["What increases glucose uptake in muscle but, decreases glucose production in the liver?\n" , 
    "What classification of OAD (Oral Anti-diabetic) medication delays the absorbtion of carbohydrates from the GI TRACT?\n" , 
    "What decreases the rate of liver glucose production, augments glucose uptake by tissues and lowers lipids?\n" , 
    "What Hyperglycemic medication increases blood glucose with in 5 - 20 minutes?\n" , 
    "What stimulates rapid and short lived release of insulin from the pancreas\n" , 
    "Amaryl is in what class of oral antidiabetic agents?\n" , 
    "The generic name of Amaryl is?\n" , 
    "In general what is the role of bolus insulin in the treatment of type1 diabetes\n" , 
    "Humalog 75/25 is comprised of:\n" , 
    "For patients with type 1 diabetes approximately what percentage of their daily insulin dose should be in the form of basal insulin\n"],
]

## ANSWERS ## 

answers = [
    ## 1 - CARDIAC DRUGS ANSWERS ## 
    ["vasodilator",
    "intropin",
    "False",
    "antidysrhythmic",
    "fentanyl",
    "True",
    "norepinephrine",
    "lidocaine",
    "epinephrine",
    "norepinephrine"],

    ## 2 - RESPIRATORY DRUGS ANSWERS ##
     ["Cromolyn Sodium(intal)",
     "True",
     "Yes",
     "Aminopentamide",
     "Doxapram",
     "Trimeprazine",
     "Reverse Analgesia",
     "Albuterol"],

     ## 3 - NEURO DRUGS ANSWERS ##
     ["Increased blood pressure",
     "Carbamazepine",
     "15-40mg/ml",
     "Constipation",
     "Grapefruit",
     "Opiod Analgesic",
     "Doxapram (Dopram)",
     "Pyridoxine (vitamin B6)",
     "10-20mcg/ml",
     "Cholinergic agents"],

     ## 4 - DIABETES DRUGS QUESTIONS ##
     ["Thiazolidinediones",
     "Alpha- Glucosidase",
     "Metformin\n`",
     "Glucagon",
     "Meglitinides",
     "Sulfonylurea",
     "Glimepiride",
     "To lower the plasma glucose spikes that result from eating",
     "75% lispro protamine (NPL) 25% lispro",
     "50%"]
]

### CATEGORIES ####


categories =["cardiac" ,  "respiratory" , "nervous" , "diabetes"]
greetings = [
            "Let's get your heart pumping...the cardiac drugs!" , 
            "Take a second to clear your throat...make way for the respiratory drugs!" ,
            "Come on, think on it....on to the nervous system drugs" , 
            "Bring your insulin...the diabetees drugs."
            ]

## GLOBAL GAME SETTINGS ## 

points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']
category = 0

## RESET ZONE ##

def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''

    global points
    global name

    points = 0
    name = None
# end-function #


## GAME INTRO ZONE ##

def game_intro():
    '''
    Welcome the player and ask him for his name as long as he thinks is correct.
    '''

    print("\n       ------ !! Welcome to the Pharmacology 101 Trivia Game !! ------\n")
    
    global name
    global category

    while name == None:
        name = input("What's your name? ")
        print("Welcome, "+name+", to the Pharmacology 101 Trivia Game!")
        correct = input("Did we get your name right? ")
        if yes.count(correct) == True: ##"Yes" or ok == "yes" or ok == "YES":
            print("Perfect, let's move on!\n")
        else:
            print("Eh?? Try again and confirm with Yes!")
            name = None

        list_categories() 
        start_system()

# end-function #
            
## GAME PLAY ZONE ##

def print_play_status(x):
    '''
    just print out the current score and the current challenge number.
    '''

    global points
    print("At the moment your total points are", points)
    print("Challenge", x+1, "\n")

# end-function #

def start_system() : 
    
    system = int(input("Pick a category by typing a number (0 to exit) : 1-4\n"))
    if system == 0 : 
        game_end()
    else :
        print(greetings[system - 1])
        start_category(system)
   
def start_category(cat) : 
    global category
    category = cat
    
    game_play()
    
def list_categories() : 
    
  # loop through categories array and print categories #
  for c in categories : 
      print(categories.index(c) + 1 , " : " , c)

def play_quest(x):
    '''int -> int
    this functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''
    global points
    global questions
    global answers
    answerPlayer = input(questions[category - 1][x])
    if answerPlayer.lower() == answers[category - 1][x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[category - 1][x], ". Next question...\n")
    last_cat = len(questions[category - 1])
    if x == last_cat -1 : 
        global categories
        
        global greetings
        
        categories.pop(category - 1)
        greetings.pop(category - 1)
        questions.pop(category - 1)
        answers.pop(category - 1)
        if len(categories) == 0 : 
            game_end()
        else:
            list_categories() 
            start_system()

# end-function #

def game_play():
    '''
    first : tell the player his current score and the current challenge number
    second: tell the play_quest-function how many and which questions it must asks the player.
    '''
   
    for x in range(len(questions[category - 1])):
        print_play_status(x)
        play_quest(x)

# end-function #

## GAME END ZONE ##

def game_end():
    '''
    first : tell the player his finish score.
    second: ask the player if wants to play again and fullfil his wish.
    '''

    print("\nYou finished the game with a total of", points, "points! \n")

    again = None
    
    while again == None:
        again = input("Play again? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            print("        Congratulations!  You've completed the game."      )
            print("            https://github.com/ksu-hmi/Pharmacology_101_Trivia"       )
            print("     ")
            print("  at the following address:       ")
            print("                                                         ")
            print("                   Thanks for playing!"                    )
            print("                ------ !! B Y E !! ------                ")
            
        else:
            print("oh, just yes or no!")
            again = None

# end-function #
    
## GAME CONTROL ZONE ##

def game_control():
    '''
    Control the whole game with these single steps.
    '''
    game_reset()
    game_intro()
    
    #start_system()
   
    #game_play()
    #game_end()
# end-function #

## FIRST GAME START ZONE ##

game_control()