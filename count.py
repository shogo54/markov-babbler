import sys


def makeWordList(filename):
    # use [] to create a new empty list
    wordlist = []
    # iterate through each line of the file
    for line in open(filename):
        # strip empty space(s) from the right of the string
        line = line.rstrip()
        # iterate through each word, using space as the delimiter to split the line
        for word in line.split(' '):
            # add each word in the wordlist
            wordlist.append(word)
    return wordlist


def main():
    # demonstrate the use of the len() function, which works with almost anything
    # in Python, such as list and dictionary
    if len(sys.argv) < 2:
        # Note that printing to stderr doesn't automatically include a whitespace
        # also, sys.argv[0] is the name of the script that was invoked
        print('Usage: {} <filename>\n'.format(sys.argv[0]))
        sys.exit(1)
    filename = sys.argv[1]
    allwords = makeWordList(filename)
    numthe = 0
    for word in allwords:
        if word == 'the':
            numthe += 1
    # print, using the weird syntax for a printf-style format string
    print('num words={} num "the"={}'.format(len(allwords), numthe))


# This code runs the main method only if this file was invoked.
# Thus, if this file is imported by another file
# it will not automatically run the main method.
if __name__ == '__main__':
    main()
