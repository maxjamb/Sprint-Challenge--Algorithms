'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# * Your function should take in a signle parameter (a string `word`)
# * Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
# * Your function must utilize recursion. 
#   * It cannot contain any loops.

def count_th(word, idx=0):
    tested_words = []
    if len(word) <= 1:
        return 0
    else: 
        if word[0] == 't' and word[1] == 'h':
            return 1 + count_th(word[2:])
        else: 
            return 0 + count_th(word[1:])


# word.strip('th')

