# GREStudy

  This is be a project implmented in Kivy to practice GRE vocab words. 
  Utilizing python NLTK library to create questions from list of GRE words. The questions are defintion, synoymn, antoymn. 
  Finally ~20 books were downloaded from gutenberg.org. Sentences were processed for the GRE words.
  Using these sentences, questions of fill in the blank were created. 

  
  Main contains code for inputting random GRE word and outputting a question, the answer and decoy answers. This is sent
  to kivy to generate GUI.
     
  Kivy_SM is the file containing all of the Kivy code

Bugs:
  Quit button does not work.
  
  Game will crash if user clicks the correct answer reveal after an wrong guess.
