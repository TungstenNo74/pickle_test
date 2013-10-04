import cPickle as pickle

best_ever = {
             'football player': "Peyton Manning",
             'Teacher':'Mr. McClure', 
             'TV Show':'Simpsons'
             }

pickle.dump(best_ever, open('save.tap', 'wb'))