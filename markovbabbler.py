import sys
import random


def get_start_states(filename, ngram_size):
    '''
    Return a list of the states that can start a new sentence. If a state
    is used to start a sentence multiple times, it should also be in the list
    multiple times.
    '''

    start_states = []
    word_list = []
    # put all the words in the word list
    for line in open(filename):
        line = line.rstrip()
        for word in line.split(' '):
            word_list.append(word)

    # put the first ngram in the startstates
    first_ngram = ' '.join(word_list[:ngram_size])
    start_states.append(first_ngram)

    # consider all of the words based on punctuation
    # count is the number of the adjacent word to the current word
    count = 0
    for word in word_list:
        count += 1
        for punct in ['.', '!', '?']:
            if word == punct and count + ngram_size < len(word_list):
                start_states.append(' '.join(word_list[count:count + ngram_size]))
    return start_states


def get_possible_words(filename, ngram_size, state):
    '''
    Use the text contained in the file with given filename to create a map
    of ngrams of the given ngram size. Then return the list of all words that
    could follow the given state. For example, for test_cases/test1.txt, with
    ngram size of 2 and the state "this is", we should return the list:
    ['an', 'great', 'great'] (or something like this in a different order).
    '''

    # main part is in get_word_dict
    dict = get_word_dict(filename, ngram_size)
    return dict[state]


def get_word_dict(filename, ngram_size):
    dict = {}
    word_list = []

    # put all the words in the word list
    for line in open(filename):
        line = line.rstrip()
        for word in line.split(' '):
            word_list.append(word)

    # put all of the ngrams one by one
    for index in range(len(word_list)):
        if index + ngram_size < len(word_list):
            ngram = ' '.join(word_list[index:index + ngram_size])
            next_word = word_list[index + ngram_size]
            if ngram not in dict:
                dict[ngram] = []
            dict[ngram].append(next_word)

    return dict


def babble(filename, ngram_size, num_sentences):
    '''
    Generate the given number of sentences using the given ngram size.
    Create a dictionary where keys are each n-1 words, and the values
    are the words that can follow in a list. Randomly pick a word, generate
    a new key, and continue until you reach a stop token (such as . or !)
    '''

    start_states = get_start_states(filename, ngram_size)
    dict = get_word_dict(filename, ngram_size)
    sentences = []
    for i in range(num_sentences):
        first_ngram = random.choice(start_states)
        word_list = first_state_list(first_ngram)
        end = False
        count = 0
        while end is False:
            ngram = ' '.join(word_list[count:count + ngram_size])
            next_word = random.choice(dict[ngram])
            word_list.append(next_word)
            count += 1
            if next_word == '.' or next_word == '!' or next_word == '?':
                end = True
        sentences.append(' '.join(word_list).lstrip())
    return sentences


def first_state_list(string):
    word_list = []
    for word in string.split(' '):
        word_list.append(word)
    return word_list


def main():
    filename = 'test_cases/shakespeare.txt'
    ngram = 2
    num_sentences = 10
    if len(sys.argv) > 3:
        filename = sys.argv[1]
        ngram = int(sys.argv[2])
        num_sentences = int(sys.argv[3])
    print('generate {} sentences from file {} using ngram size {}'.format(
        num_sentences, filename, ngram))

    sentences = babble(filename, ngram, num_sentences)
    for sentence in sentences:
        print sentence


def test1():
    filename = 'test_cases/test1.txt'
    ngram = 2
    num_sentences = 2

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
    sentences = babble(filename, ngram, num_sentences)
    for sentence in sentences:
        print sentence


if __name__ == '__main__':
    # test1()
    main()
