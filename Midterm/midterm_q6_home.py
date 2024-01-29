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

import time as times

def speed(my_func):
    def slave(*args, **kwargs):
        start = times.time()
        result = my_func(*args, **kwargs)
        end = times.time()
        time = (end-start) * 1000
        print("The function spent {time}ms to run!".format(time=time))
        return result, time

    return slave



import random

@speed
def take_info(my_word):
    print("Word: ", my_word)
    return input("Type the word: ")

my_times = []
game_over = False
level = 1

for i in range(5):
    right_word = False
    current_time = 0
    my_word = my_words[random.randint(0, len(my_words)-1)]
    while not game_over:
        #level += 1
        while not right_word:
            result, time = take_info(my_word)

            if level == 1:
                my_words_filter = filter(lambda item: len(item)<=6,my_words)
                my_words_filter = list(my_words_filter)
                my_word = my_words[random.randint(0, len(my_words)-1)]
                current_time += time
                
##                if current_time > 8:
##                    game_over  = True
               
            if level == 2:
                my_words_filter = filter(lambda item: len(item)<=10,my_words)
                my_words_filter = list(my_words_filter)
                my_word = my_words[random.randint(0, len(my_words)-1)]
                current_time += time
##                if current_time > 8:
##                    game_over  = True

            if level == 3:
                my_word = my_words[random.randint(0, len(my_words)-1)]
                current_time += time

        
        #current_time += time -> Same
        if result==my_word:
            current_time += time
            my_times.append(current_time)
            level += 1
            right_word = True
        else:
            current_time += time
            if current_time > 8:
                game_over  = True
            print("Wrond Answer!")

print(my_times)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.plot(x, my_times)
plt.xlabel('Words')
plt.ylabel('Times')
plt.title('Game result')

##
##
##        ------------------------------
##
##import random
##import time as times
##import matplotlib.pyplot as plt
##
##my_words = [
##    # Your word list here...
##]
##
##def speed(my_func):
##    def slave(*args, **kwargs):
##        start = times.time()
##        result = my_func(*args, **kwargs)
##        end = times.time()
##        time = (end - start) * 1000
##        print("The function spent {time}ms to run!".format(time=time))
##        return result, time
##
##    return slave
##
##def take_info(my_word):
##    print("Word: ", my_word)
##    return input("Type the word: ")
##
##def play_game(level):
##    if level == 1:
##        max_word_length = 6
##        max_time_allowed = 8
##    elif level == 2:
##        max_word_length = 10
##        max_time_allowed = 8
##    elif level == 3:
##        max_word_length = float("inf")
##        max_time_allowed = float("inf")
##    else:
##        print("Invalid level choice.")
##        return
##
##    my_times = []
##
##    for i in range(5):
##        right_word = False
##        current_time = 0
##        my_word = my_words[random.randint(0, len(my_words) - 1)][:max_word_length]
##
##        print(f"Level {level}, Word {i + 1} of 5")
##        while not right_word and current_time < max_time_allowed * 1000:
##            result, time = take_info(my_word)
##            current_time += time
##            if result == my_word:
##                my_times.append(current_time)
##                right_word = True
##            else:
##                print("Wrong Answer!")
##
##    if len(my_times) == 5:
##        print("Game completed successfully.")
##        print(my_times)
##
##        x = [1, 2, 3, 4, 5]
##        plt.plot(x, my_times)
##        plt.xlabel('Words')
##        plt.ylabel('Times')
##        plt.title('Game result')
##        plt.show()
##    else:
##        print("Game over!")
##
##level = int(input("Choose the game level (1, 2, or 3): "))
##play_game(level)
##
