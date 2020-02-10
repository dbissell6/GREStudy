"""
Created on Sun Sep 15 21:27:06 2019

@author: dab
"""

import pandas as pd
import random
from nltk.corpus import wordnet
from pathlib import Path


# =============================================================================
# Set of functions to make vocab games. 
# =============================================================================

## Definitions, Synonyms, antonyms, Sample Sentences, 

# import from excel to dataframe

script_location = Path(__file__).parent
csv_path = script_location / 'vocabulary.csv'
gre = pd.read_csv(csv_path)

###############################################################################


##### The game function should return 0) The question, 1) the answer, 2) 3 decoys,
#####  3)  


##############################################################################
#### Create a dataframe for the individual that tracks how often they get a word
#### right or wrong
#### lexadex
##############################################################################

indy = pd.DataFrame()
indy['words'] = GRE['words']
indy['correct'] = 0
indy['tries'] = 0

"""Set index to word"""
indy.set_index("words",inplace=True)


###############################################################################
### update lexadex
### function at each game

def update_score(l):
    
    thing = l
    indy.loc[thing[0]].at['correct']+=thing[1]
    indy.loc[thing[0]].at['tries']+= 1
    ### Save
    indy.to_excel("vocadex.xlsx")
    

# Create 3 decoys
    
def decoys(synonyms):
    d1, d2, d3 = False, False, False
    
    while d1== False and d2 == False and d3 == False:
    
        d1o = GRE.words[random.randint(0,len(GRE))]
        if d1o not in synonyms:
            d1 = d1o
                
        d2o = GRE.words[random.randint(0,len(GRE))]
        if d2o not in synonyms:
            d2 = d2o
            
        d3o = GRE.words[random.randint(0,len(GRE))]
        if d3o not in synonyms:
            d3 = d3o
    
    return d1,d2,d3

###      Games

##############################################################################
### Samp_Sent_Game
##############################################################################

   ''' 
   an example sentence will appear with target word replaced as ???
   option will consist of correct word and 3 decoys.
   #  usa is a corpus 
   usa -- list of tuples containing example sentence and correct responses
   sent --
   tup --
   word --
   
   '''


def samp__sent_game():
    
    usa = ha   
    tup = usa.sample() 
    sent = tup.iat[0,0]
    sent = sent.replace('\n', ' ')
    word = tup.iat[0,1]
    word = word.strip(' ')
    
    ### Replace target with question marks
    sent = sent.replace(word, '???')
    
    
    synonyms = []
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            if l.name() in GRE.words.values and word != l.name():
                synonyms.append(l.name()) 
    
    
    synonyms = list(set(synonyms)) 
    
    d1, d2, d3 = decoys(synonyms)
    
    final = [word,d1,d2,d3]
    
    random.shuffle(final)
    
    return sent, word, final
    

##############################################################################
### def_Game

### a definition appears with 3 decoys

##############################################################################


def def_Game():
  
    synonyms = []
    
    word = GRE.words[random.randint(0,len(GRE)-1)]
    define=wordnet.synsets(word)
    
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            if l.name() in GRE.words.values and word != l.name():
                synonyms.append(l.name()) 

    synonyms = list(set(synonyms)) 
    
    
    d1, d2, d3 = decoys(synonyms)
    
    final = [word,d1, d2, d3]
    
    random.shuffle(final)
    
    q = 'Which word means "{0}"'.format(define[0].definition())

    return q, word, final
    


##############################################################################
### syn_Game

### a program that chooses target word 4 options one being a SYNONYMN other 
### 3 are randos making sure not a synymn
### all words are GRE words, 
### should change this to make it easier
##############################################################################

def syn_Game():

  
    synonyms = [] 

    while len(synonyms) == 0:  
        x = GRE.words[random.randint(0,len(GRE)-1)]
        for syn in wordnet.synsets(x): 
            for l in syn.lemmas(): 
                if l.name() in GRE.words.values and x != l.name():
                    synonyms.append(l.name()) 

        synonyms = list(set(synonyms)) 
    
    if len(synonyms)>2:
        y = synonyms[random.randint(0,len(synonyms)-1)]
    else:
        y = synonyms[0]
    

    d1, d2, d3 = decoys(synonyms)        
        
    final = [y,d1, d2, d3]
    
    random.shuffle(final)
    
    q = ('What is the synonym of {0}? '.format(x))


    return q, y, final

##############################################################################
### make a program that chooses target word + 4 options one being a ANTONYM other 
### 3 are randos making sure not a synymn
##############################################################################

def ant_Game():
    antonyms = [] 

    while len(antonyms) == 0:  
        x = GRE.words[random.randint(0,len(GRE)-1)]
        for syn in wordnet.synsets(x): 
            for l in syn.lemmas(): 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name()) 
                    antonyms_r = [word for word in antonyms if word not in x and x not in word]
                    if len(antonyms_r) <1:
                        antonyms = []
                        antonyms_r = []
      
    antonyms_r = list(set(antonyms)) 
    
    if len(antonyms_r)>2:
        y = antonyms_r[random.randint(0,len(antonyms_r)-1)]
    else:
        y = antonyms_r[0]
    
   
    d1, d2, d3 = decoys(antonyms)
                        
    final = [y, d1, d2, d3]
    
    random.shuffle(final)
    q = ('What is the antonym of {0}? '.format(x))
    
    return  q, y, final, x
# =============================================================================
#     
# =============================================================================
### Load previous game state Data frame
indy = pd.read_excel("/Users/Path/vocadex.xlsx")
### Set index to word
indy.set_index("words",inplace=True)


### Load example sentences as dataframe

csv_path = script_location / 'usa.xlsx'
ha = pd.read_csv(csv_path)

# drop first column, rename others
ha.drop(['Unnamed: 0'], axis=1,inplace=True)
ha.rename(columns={0: "sent", 1: "word"},inplace=True)

#########
# display known lexadex words
Lexadex = indy.loc[indy['tries'] >= 1]
