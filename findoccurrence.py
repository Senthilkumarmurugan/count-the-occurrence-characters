# to ind a number of characters present in a text
import pprint
text='''
type something or add some text
'''
count={}

for characters in text.upper():
    count.setdefault(characters,0)
    count[characters] +=1
    pprint.pprint(count)


