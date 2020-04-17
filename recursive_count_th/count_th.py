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
    th_count = 0
    tested_words = []
    if word == 0 or len(word) <= 1:
        return th_count
    else if word[idx] == 't' and word[idx+1] == 'h':
        th_count += 1
        tested_letters = [word[idx], word[idx+1]]
        untested_letters = word[1:]
        return count_th(untested_letters, idx+1)
    else:
        return count_th(word, idx+1)


# word.strip('th')

