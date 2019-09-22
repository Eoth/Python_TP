import pickle
def the_data():
    words_list=[
        'éloignés', 
        'poularde', 
        'flashait', 
        'ruserons', 
        'étouffez', 
        'révoquai', 
        'déjaugez',
        'entourer',
    ]
    with open('mydata','wb') as the_file:
        my_pickle = pickle.Pickler(the_file)
        my_pickle.dump(words_list)

def get_data():
    with open('mydata','rb') as the_file:
        my_unpickle = pickle.Unpickler(the_file)
        words = my_unpickle.load()
    return words
