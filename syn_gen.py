#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:27:06 2019

@author: danielbissell
"""

import pandas as pd
import random
from nltk.corpus import wordnet 


###
### Things that could be done
### 1)crossword puzzle, 
### 2)if someone is about to read a new book, pull words from that book that might 
### be out of range for the person
### 3) create analogy game with GloVe

# =============================================================================
# Set of functions to make vocab games. 
# =============================================================================

## Definitions, Synonyms, antonyms, Sample Sentences, 

# import from excel to dataframe
GRE = pd.read_csv("/Users/danielbissell/Desktop/vocabulary.csv")

###############################################################################

####################################################################
##### To do
####################################################################
#### Create new games

### In Syn_Game and Ant_Game all answers and decoy words are GRE words 
### should change this to make it easier

##### The game function should return 0) The question, 1) the answer, 2) 3 decoys,
#####  3)  


##############################################################################
#### Create a dataframe for the individual that tracks how often they get a word
#### right or wrong
#### lexadex
##############################################################################

indy_1 = pd.DataFrame()

indy_1['words'] = GRE['words']

indy_1['correct'] = 0
indy_1['tries'] = 0

### Set index to word
indy_1.set_index("words",inplace=True)


###############################################################################
### update lexadex
### function at each game

def update_score(l):
    
    thing = l
    indy_1.loc[thing[0]].at['correct']+=thing[1]
    indy_1.loc[thing[0]].at['tries']+= 1
    ### Save
    indy_1.to_excel("vocadex.xlsx")
    


#########################
###Games
##########
##############################################################################
### Samp_Sent_Game

### an example sentence will appear with target word replaced as ???
### option will consist of correct word and 3 decoys.
   # n is number of times, usa is a corpus 
##############################################################################


def Samp__Sent_Game(n,usa):

    
    ### usa is a list of tuples containing example sentence and correct responses
    usa = ha

    ### n is the number on times the game is played
    
    
    for i in range(n):
        
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
        
        
        z, zz, d3 = False, False, False
        
        while z== False and zz == False and d3 == False:
        
            zo = GRE.words[random.randint(0,len(GRE))]
            if zo not in synonyms:
                z = zo
                    
            zzo = GRE.words[random.randint(0,len(GRE))]
            if zzo not in synonyms:
                zz = zzo
                
            d3o = GRE.words[random.randint(0,len(GRE))]
            if d3o not in synonyms:
                d3 = d3o
                      
                
        final = [word,z,zz,d3]
        
        random.shuffle(final)
        
        
        return sent, word, final


##############################################################################
### Def_Game

### a definition appears with 3 decoys

##############################################################################


def Def_Game(n):

    ### n is the number on times the game is played
    for i in range(n):
        
        synonyms = []
        
        word = GRE.words[random.randint(0,len(GRE)-1)]
        define=wordnet.synsets(word)
        #word_def = (define[0].definition())
        


        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                if l.name() in GRE.words.values and word != l.name():
                    synonyms.append(l.name()) 

        synonyms = list(set(synonyms)) 
        
        
        z, zz, d3 = False, False, False
        
        while z== False and zz == False and d3 == False:
        
            zo = GRE.words[random.randint(0,len(GRE)-1)]
            if zo not in synonyms:
                z = zo
                    
            zzo = GRE.words[random.randint(0,len(GRE)-1)]
            if zzo not in synonyms:
                zz = zzo
                
            d3o = GRE.words[random.randint(0,len(GRE)-1)]
            if d3o not in synonyms:
                d3 = d3o
                      
                
        final = [word,z,zz,d3]
        
        random.shuffle(final)
        
        q = 'Which word means "{0}"'.format(define[0].definition())

    return q, word, final
    


##############################################################################
### Syn_Game

### a program that chooses target word 4 options one being a SYNONYMN other 
### 3 are randos making sure not a synymn
### all words are GRE words, 
### should change this to make it easier
##############################################################################

def Syn_Game(n):

    ### n is the number on times the game is played
    for i in range(n):
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
        
        z, zz = False, False
        
        while z== False and zz == False:
        
            zo = GRE.words[random.randint(0,len(GRE)-1)]
            if zo not in synonyms:
                z = zo
                    
            zzo = GRE.words[random.randint(0,len(GRE)-1)]
            if zzo not in synonyms:
                zz = zzo
                
            d3o = GRE.words[random.randint(0,len(GRE)-1)]
            if d3o not in synonyms:
                d3 = d3o
                      
                
        final = [y,z,zz,d3]
        
        random.shuffle(final)
        
        
        q = ('What is the synonym of {0}? '.format(x))


    return q, y, final

##############################################################################
### make a program that chooses target word + 4 options one being a ANTONYM other 
### 3 are randos making sure not a synymn
##############################################################################

def Ant_Game(n):
    
    for i in range(n):
    
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
        
        ### Selects decoys
        z, zz = False, False
        
        while z== False and zz == False:
        
            zo = GRE.words[random.randint(0,len(GRE)-1)]
            if zo not in antonyms_r:
                z = zo
                    
            zzo = GRE.words[random.randint(0,len(GRE)-1)]
            if zzo not in antonyms_r:
                zz = zzo
                
            d3o = GRE.words[random.randint(0,len(GRE)-1)]
            if d3o not in antonyms_r:
                d3 = d3o
                      
                
        final = [y,z,zz,d3]
        
        random.shuffle(final)
        q = ('What is the antonym of {0}? '.format(x))
        
        return  q, y, final, x

    
    
# =============================================================================
#     
# =============================================================================
### Load previous game state Data frame
indy_1 = pd.read_excel("/Users/danielbissell/Desktop/Python stuff/vocadex.xlsx")
### Set index to word
indy_1.set_index("words",inplace=True)


### Load example sentences as dataframe
ha = pd.read_excel("/Users/danielbissell/Desktop/Python stuff/usa.xlsx")

# drop first column, rename others
ha.drop(['Unnamed: 0'], axis=1,inplace=True)
ha.rename(columns={0: "sent", 1: "word"},inplace=True)

#########
# display known lexadex words
Lexadex = indy_1.loc[indy_1['tries'] >= 1]






