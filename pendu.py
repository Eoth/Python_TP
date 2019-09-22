from donnees import *
from fonctions import *
import random
import os
import pickle
def pendu_game():
    the_data()
    words=get_data()
    user=user_name()
    taille= os.path.getsize("C:\\Users\\pakye\\Desktop\\Projet Personnelle\\pack Pyhton\\pendu_data")
    val = False

    if taille!=0:
        with open('pendu_data','rb') as the_file:
            the_unpick=pickle.Unpickler(the_file)
            thedata=the_unpick.load()
        if thedata:
            for my_id in thedata:
                 if user == my_id:
                     val=True

    if val ==False:
        nb_rand=random.randrange(len(words))
        hidden_words=words[nb_rand]
        rest_nb=8
        score=0

        thedata={user:[hidden_words,score, rest_nb]}
        with open('pendu_data','wb') as the_file:
            the_pick = pickle.Pickler(the_file)
            the_pick.dump(thedata)
    else:
        print('************\nHeureux de te revoir\n*************')
        hidden_words=thedata[user][0]
        score=thedata[user][1]
        rest_nb=thedata[user][2]
        if rest_nb==0: 
            rest_nb=8
            score=0
    continued='o'
    stop=False
    case=['*','*','*','*','*','*','*','*']
    while rest_nb>0 and stop==False:
        print("****your score:{}, number remaining to play:{}****\n".format(score,rest_nb))
        word=play_word()
        j=0
        for a in hidden_words: 
            if a==word:
                score+=rest_nb
                case[j]=a
            j+=1
        print(case)
                
        continued=input("Are you want to continue ? tape 'o' for yes and 'n' to stop :")
        if continued=='o':
            rest_nb-=1
        else: 
            stop=True
            thedata={user:[hidden_words,score, rest_nb]}
            with open('pendu_data','wb') as the_file:
                the_pick = pickle.Pickler(the_file)
                the_pick.dump(thedata)
        if score==36:
            print('\n*********GAGNER*********\n')
        elif rest_nb==0:
            print('\n*********PENDU**********\n')
    



