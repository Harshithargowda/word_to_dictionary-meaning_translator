import json
from difflib import get_close_matches

data = json.load( open( 'data.json' ) )


def translate(w):
    w = w.lower()
    if w in data:
        return data[word]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]  #w.title() converts the word with lower letters to first word with caps
    elif w.upper() in data:
        return data[w.upper()]
    elif len( get_close_matches( w, data.keys(), cutoff=0.8 ) ) > 0:
        yn = input(
            "do u mean %s instead? if yes then Enter y, if No then enter n: " % get_close_matches( w, data.keys() )[0] )
        if yn== "y":
            return data[get_close_matches( w, data.keys())[0]]
    else:
        return "No match found,double check the word u entered"


word = input( "enter the word to be translated: " )
#print( translate( word ) )

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

