'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  # BASE CASE
  if len(word) < 2:
      return 0
  # RECURSIVE CASE
  # If first two indexes contain 'th", add one to the count - skip over the first index and compare next two adjacent indexes
  # begining for the elem in the 2nd index(i.e third position)
  elif word[:2] == "th":
      return count_th(word[2:]) + 1
  # If first two indexes dont contain 'th', just skip over the first index and compare next two adjacent indexes starting from the
  # second position (i.e index  of 1)
  else:
      return count_th(word[1:])


print(count_th("tttththththththt")) #6
print(count_th("something---ththththththt")) #7

