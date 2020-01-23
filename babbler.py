import random
import sys


class Babbler:
    """
    Markov Babbler

    After being trained on text from various authors, can
    'babble', or generate random walks, and produce text that
    vaguely sounds like the author.

    :param int n: The length of an n-gram for state
    :param starters: The list of possible starting ngrams
    :type starters: list(str)
    :param stoppers: The list of possible ending ngrams
    :type stoppers: list(str)
    :param dictionary: The dictionary mapping a ngram to the list of its successors
    :type dictionary: dict(str, list(str))
    """

    def __init__(self, n, seed=None):
        """
        The constructor for Babbler class.

        :param int n: The length of an n-gram for state.
        :param seed: The seed for a random number generation. If none given use the default.
        :type seed: int or None
        """
        self.n = n
        self.starters = []
        self.stoppers = []
        self.dictionary = {}
        if seed is not None:
            random.seed(seed)

    def add_sentence(self, sentence):
        """
        Process the given sentence.

        :param str sentence: The string separated by spaces.
            The sentence is expected to be lowercase.
        :var words: The list converted from the given sentence.
        :vartype words: list(str)
        :var str ngram: The current ngram.
        """
        # add 'EOL' (stands for 'end of line') at the end of the sentence.
        words = sentence.split() + ['EOL']
        # the first ngram is the first n words
        ngram = ' '.join(words[0:self.n])
        # add the first ngram to starters and last ngram (excluding 'EOL') to stoppers
        self.starters.append(ngram)
        self.stoppers.append(' '.join(words[-1 - self.n:-1]))

        # get each word (except for the first n words) and map ngram to the word
        # then update the ngram
        for word in words[self.n:]:
            if ngram in self.dictionary:
                self.dictionary[ngram].append(word)
            else:
                self.dictionary[ngram] = [word]
            # convert ngram to a list, get rid of the first word,
            # add a new word, and then convert back to a string
            ngram = ' '.join(ngram.split()[1:] + [word])

    def add_file(self, file_name):
        """
        Process the file with the given file_name.

        The method is assuming that the input data has already
        been pre-processed so that each sentence is on a separate line.

        :param str file_name: The name of the target file directory.
        """
        # call add_sentence() method for each line of an input file.
        for line in [line.rstrip().lower() for line in open(file_name, errors='ignore').readlines()]:
            self.add_sentence(line)

    def get_starters(self):
        """
        Return a list of all n-grams that start any sentence the program has seen.

        The resulting list may contain duplicates because one n-gram may start
        multiple sentences.

        :return starters: The list of possible starting ngrams
        :rtype starters: list(str)
        """
        return self.starters

    def get_stoppers(self):
        """
        Return a list of all n-grams that stop any sentence the program has seen.

        The resulting value may contain duplicates because one n-gram may stop
        multiple sentences.

        :return: The list of possible ending ngrams
        :rtype: list(str)
        """
        return self.stoppers

    def get_successors(self, ngram):
        """
        Return a list of words that may follow the given n-gram.
        If the given state never occurs, return an empty list.

        The resulting list may contain duplicates, because each
        n-gram may be followed by different words.

        For example, suppose an author has the following sentences:
        'the dog dances quickly'
        'the dog dances with the cat'
        'the dog dances with me'

        If n=3, then the n-gram 'the dog dances' is followed by
        'quickly' one time, and 'with' two times.

        :param str ngram: The ngram to search its successors
        :return: The list of words that may follow the given n-gram.
        :rtype: list(str)
        """
        if self.has_successor(ngram):
            return self.dictionary[ngram]
        else:
            return []

    def get_all_ngrams(self):
        """
        Return all the possible n-grams that the program has seen
        across all sentences.

        :return: All the possible n-grams
        :rtype: dictionary view object
        """
        return self.dictionary.keys()

    def has_successor(self, ngram):
        """
        Return True if the given ngram has at least one possible successor
        word, and False if it does not.

        :param str ngram: The ngram to search if its successors exist or not
        :return: If the give ngram has at least one successor
        :rtype: bool
        """
        return ngram in self.dictionary

    def get_random_successor(self, ngram):
        """
        Given an n-gram, randomly pick from the possible words
        that could follow that n-gram.

        The randomness should take into account how likely
        a word is to follow the given n-gram.
        For example, if n=3 and the program is train on these three sentences:
        'the dog dances quickly'
        'the dog dances with the cat'
        'the dog dances with me'
        and get_random_next_word() is called for the state 'the dog dances',
        the program returns 'quickly' about 1/3 of the time, and 'with' 2/3 of the time.

        :param str ngram: The ngram to get its random successor
        :return: The randomly selected word that could follow the given ngram
        :rtype: str
        """
        return random.choice(self.get_successors(ngram))

    def babble(self):
        """
        Generate a random sentence based on the trained texts

        :var str ngram:
        :var sentece: The list of sequenced words generated so far
        :vartype sentence: list(str)
        :return: A random sentence generated based on the trained texts
        :rtype: str
        """
        # pick a starter ngram. This is the current ngram
        ngram = random.choice(self.starters)
        sentence = [ngram]

        # if the current ngram is in stoppers, then return the sentence.
        # otherwise, pick a random successor word based on the current ngram,
        # add the successor to the end of the sentence,
        # update the ngram, and repeat the generating process.
        while ngram not in self.stoppers:
            successor = self.get_random_successor(ngram)
            sentence.append(successor)
            ngram = ' '.join(ngram.split()[1:] + [successor])

        return ' '.join(sentence)


def main(n=3, file_name='tests/test2.txt', num_sentences=5):
    """
    Simple test driver.
    """
    babbler = Babbler(n)
    babbler.add_file(file_name)
    print(file_name)
    print(f'num starters {len(babbler.get_starters())}')
    print(f'num ngrams {len(babbler.get_all_ngrams())}')
    print(f'num stoppers {len(babbler.get_stoppers())}')
    for _ in range(num_sentences):
        print(babbler.babble())


if __name__ == '__main__':
    # remove the first parameter, which should be babbler.py, the name of the script
    sys.argv.pop(0)
    n = 3
    file_name = 'tests/test2.txt'
    num_sentences = 5
    if len(sys.argv) > 0:
        n = int(sys.argv.pop(0))
    if len(sys.argv) > 0:
        file_name = sys.argv.pop(0)
    if len(sys.argv) > 0:
        num_sentences = int(sys.argv.pop(0))
    main(n, file_name, num_sentences)
