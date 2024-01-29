'''
- Using the concepts saw in class (decorator), create a program that
will show a random word from a list to the user and the user must type the word.
- If the user types wrong, ask the user to type again the same word,
when the word is correct, save the time that the user spent inside an array.
- The program must show 5 words to the user and finishes when the user types right the 5 words.
- At the end the program must show a chart with the user times.
You will need to import the library random and use the function:
random.randint(start, stop)
For this you will need to install the python matplotlib:
in cmd type -> pip install matplotlib
'''

import random
import time as times
import matplotlib.pyplot as plt


my_words = [
"abacaxi",
"abgesang",
"abiuret",
"advocaat",
"aitch",
"aloisiite",
"atlatl",
"autochthonous",
"bdelloid",
"bhagavata",
"bhikku",
"bobbejaan",
"cassioberry",
"catapleiite",
"chhatri",
"chiaroscurist",
"chihuahua",
"chlorophyll",
"chthonic",
"cixiid",
"cnemidocoptes",
"cnidoblast",
"coelacanth",
"courtoisie",
"crwth",
"ctenii",
"cywydd",
"dhole",
"dvandva",
"Dzungar",
"eczema",
"egueiite",
"Eichhornia",
"eudaemonic",
"fjeld",
"gnathonic",
"gneissoid",
"gnomonic",
"gnosticize",
"jharal",
"Kharijite",
"khedive",
"kiekie",
"kierkegaardian",
"knaidlach",
"Kwakiutl",
"logorrhea",
"mbira",
"mlechchha",
"Myxosporidiida",
"ngege",
"ngwee",
"periscii",
"pfeffernuss",
"pfennig",
"phalaenopsid",
"phthalein",
"phthisis",
"prosciutto",
"pschent",
"psephology",
"pseudaxis",
"psittaceous",
"psoriasis",
"ptarmic",
"pterodactyl",
"ptosis",
"pycnogonid",
"qiviut",
"rhathymia",
"rhotacismus",
"rijksdaalder",
"rygbere",
"sacrilegious",
"schokker",
"sforzando",
"sgabello",
"shanghaiing",
"sjambok",
"soubrette",
"staphylococci",
"svedberg",
"synecdoche",
"taaffeite",
"taeniid",
"takkanah",
"tchaviche",
"teonanacatl",
"tjaele",
"tsao",
"Tsingtao",
"tzigane",
"Ursprache",
"vignette",
"volksraad",
"vrbaite",
"weltanschauung",
"ylem",
"ytterbium",
"zuurveldt",
"zwetschenwasser"
]

user_times = []

def spent_time(my_func): #this is the decorator 
    def slave(*args, **kwargs):
        start = times.time()
        my_func(*args, **kwargs) #passed from parameter
        end = times.time()
        time = (end-start)
        user_times.append(time)
        #print("The function spent {time}ms to run!".format(time=time))
    return slave

@spent_time
def my_func(my_words):
##    count = 0
##    while count < 5:
##        word_index = random.randint(0, len(my_words)-1)
##        rnd_word = my_words[word_index]
##        #print("Random word:", rnd_word)
##        start = times.time()

        user_input = input(f"Type the word '{rnd_word}': ")
        #end = times.time()
        while user_input != rnd_word:
            user_input = input(f"Wrong! Type again the word '{rnd_word}': ")

            #print("\tIncorrect word typed. Try again:")

for i in range(5):
    rnd_word = my_words[random.randint(0, len(my_words) - 1)]
    my_func(rnd_word)
    
def my_chart():
    plt.plot(user_times, marker='o', linestyle='-')
    plt.ylabel('Time (ms)')
    plt.xlabel('Word Number')
    plt.title('User Input Times')
    plt.show()

my_func(my_words)
my_chart()



