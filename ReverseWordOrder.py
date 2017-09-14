# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

phrase = input("Enter a long string with multiple words: ")

phraselist = phrase.split()
phraselist.reverse()
reverselist = " ".join(phraselist)
print(reverselist)
