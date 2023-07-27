
# some quotations

great_quotes = (
    "And we danced, on the brink of an unknown future, to an echo from a vanished past. (John Wyndham) \n" + \
    "Life is what happens to you while you're busy making other plans. (wrongly attributed to John Lennon)\n" + \
    "You cannot overestimate the unimportance of practically everything. (John Maxwell)"
)
quotesList = []

quotesList = great_quotes.split('\n')

for quoteNumber in range(0,3,1):
    countWords = len(quotesList[quoteNumber].split())
    longestWord = max(quotesList[quoteNumber].split(),key=len).upper()
    print(quotesList[quoteNumber], "has", countWords, "words, the longest which is", longestWord, "\n")

#def get_words(greatquotes):
#    greatquotes = greatquotes.replace("\n","")
#    return greatquotes

#def count_words(countwords):
#    countwords = len(newLineRemoved.split())
#    return countwords

# Ophakken in 3 quotes
# Door de functions laten lopen


