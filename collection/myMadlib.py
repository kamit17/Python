"""                                       
Once upon a time, deep in an ancient jungle,
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
"""                                                 
storyFormat ='''Once {people} went on a journey together. On their way 
there was a deep {place}. There was no {item}; so they swam across 
the {place}. They all got safely to the other bank. 

“Are we allsafe?” asked one of the Wise Men, 

“Let us count and see,” said the others. 

The first man counted, “One, two, three, four, five,” and 
said, “Look ! one of us is missing. There are only five of us here.” 
He counted only the others. 

“You are silly,” said a second Wise Man. “Let me count, 
'''
def tellStory():                                      
    userPicks = dict()                              
    addPick('people', userPicks)            
    addPick('place', userPicks)            
    addPick('item', userPicks)            
    story = storyFormat.format(**userPicks)
    print(story)
                                                    
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Fill the blank for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response                                                             

tellStory()                                         
input("Press Enter to end the program.")        
