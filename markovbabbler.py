import sys
import random


def get_start_states(filename, ngramsize):
    '''Return a list of the states that can start a new sentence. If a state
    is used to start a sentence multiple times, it should also be in the list
    multiple times.
    '''

    # TODO: return all start states from the file
    return ['start state 1', 'start state 2', 'start state 1']


def get_possible_words(filename, ngramsize, state):
    '''Use the text contained in the file with given filename to create a map
    of ngrams of the given ngram size. Then return the list of all words that
    could follow the given state. For example, for test_cases/test1.txt, with
    ngram size of 2 and the state "this is", we should return the list:
    ['an', 'great', 'great'] (or something like this in a different order).
    '''

    # TODO: return all the words that could follow the given state
    return ['dog', 'cat', 'dog', 'bird']


def babble(filename, ngramsize, numsentences):
    '''Generate the given number of sentences using the given ngram size.
    Create a dictionary where keys are each n-1 words, and the values
    are the words that can follow in a list. Randomly pick a word, generate
    a new key, and continue until you reach a stop token (such as . or !)
    '''

    # TODO: return sentences from the file
    return ['sentence one', 'sentence two']


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
    ngram = 3
    numsentences = 2

    possible_words = get_possible_words(filename, ngram, 'this is')
    assert('an' in possible_words)
    assert(possible_words.count('great') == 2)

    start_states = get_start_states(filename, ngram)
    assert('This is' in start_states)
    # TODO: you should check other possible start states

    # setting a seed for the random number generator means that the sequence
    # of pseudo-random numbers is the same for each run of the code.
    random.seed(0)
    # TODO make sure the sentences you generate make sense
    sentences = babble(filename, ngram, numsentences)
    for sentence in sentences:
        print(sentence)


if __name__ == '__main__':
    test1()
    # main()
