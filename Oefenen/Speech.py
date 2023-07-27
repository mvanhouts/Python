
# Julius Caesar Act 4, Scene 3, 218–224
brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."

brutus_speech = brutus_speech.replace('\n','')
brutus_speech = brutus_speech.replace(';','')
brutus_speech = brutus_speech.replace(',','')
brutus_speech = brutus_speech.replace('.','')

wordsDictionary = {}

for word in brutus_speech.split():
    wordsDictionary[len(word)] = []


for word in brutus_speech.split():
    wordsDictionary[len(word)].append(word)

    
for keysSorted,value in wordsDictionary.items():
    print(keysSorted,"-Letter words =",len([item for item in value if item]))

