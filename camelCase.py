sentence = input('Enter a sentence here that will be turned into camelCase: ').title()
# title makes this first letter into a capital

sentenceList = sentence.split( )

sentenceList2 = ("".join(sentenceList))

camelCase = sentence[0:1].lower() + sentenceList2[1:]

print(camelCase)