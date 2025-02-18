
def count_overlapping_occurrences(sentence, word):
    # Convert both sentence and word to lowercase 
    word = word.lower()
    sentence = sentence.lower()
    wordlen = 0
    sentlen = len(sentence)
    count = 0
    ind = 0
    while ind != -1:
        ind = sentence.find(word, ind+wordlen)
        print('index = ', ind)
        wordlen = len(word)
        count += 1
    return count

# Example usage
sentence = "TodisplayinginthehouseofTodwiththeTod"
word = "Tod"
print(count_overlapping_occurrences(sentence, word))  # Output: 4
