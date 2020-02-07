# GREStudy

  This is be a project implemented in Kivy to practice GRE vocab words. 
  Utilizing python NLTK library to create questions from list of GRE words. The questions are defintion, synonym, antonym. 
  Finally ~20 books were downloaded from gutenberg.org. Sentences were processed for the GRE words.
  Using these sentences, questions of fill in the blank were created. 
  
  
  vocabulary.csv - two columns of GRE words and definition. Defs are not used, made by NLTK
  
  usa.xlsx - List of target GRE word and sentences containing that word found in books
  
  syn_gen.py -  contains code for inputting random GRE word and outputting a question, the answer and decoy answers. This is     
  sent to kivy to generate GUI.
     
  Kivy_SM - python file containing all of the Kivy code

  The game will record score in a file called vocadex.xlsx. 




Bugs:
  Quit button does not work.
  
  Game will crash if user clicks the correct answer reveal after an wrong guess.
