import sys
import random


def get_start_states(filename, ngramsize):
    '''Return a list of the states that can start a new sentence. If a state
    is used to start a sentence multiple times, it should also be in the list
    multiple times.
    '''

    startstates = []
    wordlist = []
    # put all the words in the word list
    for line in open(filename):
        line = line.rstrip()
        for word in line.split(' '):
            wordlist.append(word)

    # put the first ngram in the startstates
    firstngram = ' '.join(wordlist[:ngramsize])
    startstates.append(firstngram)

    # consider all of the words based on punctuation
    # count is the number of the next word of the current word
    count = 0
    for word in wordlist:
        count += 1
        for punct in ['.', '!', '?']:
            if word == punct and count + ngramsize < len(wordlist):
                startstates.append(' '.join(wordlist[count:count + ngramsize]))
    return startstates


def get_possible_words(filename, ngramsize, state):
    '''Use the text contained in the file with given filename to create a map
    of ngrams of the given ngram size. Then return the list of all words that
    could follow the given state. For example, for test_cases/test1.txt, with
    ngram size of 2 and the state "this is", we should return the list:
    ['an', 'great', 'great'] (or something like this in a different order).
    '''

    possiblewords = []
    wordlist = []
    # put all the words in the word list
    for line in open(filename):
        line = line.rstrip()
        for word in line.split(' '):
            wordlist.append(word)

    # consider all of the words one by one
    for index in range(len(wordlist)):
        current = ' '.join(wordlist[index:index + ngramsize])
        if current == state:
            possiblewords.append(wordlist[index + ngramsize])
    return possiblewords


def babble(filename, ngramsize, numsentences):
    '''Generate the given number of sentences using the given ngram size.
    Create a dictionary where keys are each n-1 words, and the values
    are the words that can follow in a list. Randomly pick a word, generate
    a new key, and continue until you reach a stop token (such as . or !)
    '''

    # TODO: return sentences from the file
    sentences = []
    for i in range(numsentences):
        firstngram = random.choice(get_start_states(filename, ngramsize))
        wordlist = first_state_list(firstngram)
        end = False
        count = 0
        while end == False:
            current = ' '.join(wordlist[count:count + ngramsize])
            next = random.choice(get_possible_words(filename, ngramsize, current))
            wordlist.append(next)
            count+=1
            if next == '.' or next == '!' or next == '?':
                end = True
        sentences.append(' '.join(wordlist))
    return sentences

def first_state_list(string):
    wordlist = []
    for word in string.split(' '):
        wordlist.append(word)
    return wordlist

def main():
    filename = 'test_cases/test1.txt'
    ngram = 3
    numsentences = 2
    if len(sys.argv) > 3:
        filename = sys.argv[1]
        ngram = int(sys.argv[2])
        numsentence = int(sys.argv[3])
    print('generate {} sentences from file {} using ngram size {}'.format(
        numsentences, filename, ngram))

    sentences = babble(filename, ngram, numsentences)
    for sentence in sentences:
        print(sentence)


def test1():
    filename = 'test_cases/test1.txt'
    ngram = 2
    numsentences = 2

    possible_words = get_possible_words(filename, ngram, 'this is')
    assert ('an' in possible_words)
    assert (possible_words.count('great') == 2)
    for i in possible_words:
        print i

    start_states = get_start_states(filename, ngram)
    assert ('This is' in start_states)
    assert ('And this' in start_states)
    assert ('This sentence' in start_states)
    assert ('And finally' in start_states)
    assert ('Of course' in start_states)
    for i in start_states:
        print i

    # setting a seed for the random number generator means that the sequence
    # of pseudo-random numbers is the same for each run of the code.
    random.seed(0)
    # TODO make sure the sentences you generate make sense
    sentences = babble(filename, ngram, numsentences)
    for sentence in sentences:
        print(sentence)


if __name__ == '__main__':
    # test1()
    main()
