# Lab: Markov Babbler

For this assignment, we will build a “Markov Babbler” that uses
[Markov Chains](https://en.wikipedia.org/wiki/Markov_chain)
to “babble” random things.

We will train our babbler on a large amount of text (usually called a _corpus_), and then have it generate random sentences that sound vaguely like they were written by the same author as the training set.

**Note** Don’t train your babbler on racist tweets or it could end up sounding like Microsoft’s now-defunct
[Nazi-sympathizing, Holocaust-denying Twitter-bot Tay](http://theantimedia.org/microsofts-new-twitter-bot-becomes-nazi-sympathizing-maniac-within-24-hours/),
which probably used something like Markov Chains in its implementation.

The complete works of Shakespeare is available [in a huge text file here](https://drive.google.com/open?id=0B8YG7KPaRWn7bXEwUDlOSEV6QXc) (only visible on campus), or you can use any large amount of text you are interested in. [Project Gutenberg](http://www.gutenberg.org/)
online has a ton of this sort of thing available, although you will have to process it somewhat to get it into the right format by breaking out all of the punctuation.

The starter Python program is `markovbabbler.py`. Please make sure to keep the `babble()`, `get_start_states()`, and `get_possible_words()` functions with their current signatures and the main() function as the top-level function. Other than that you can create as many helper functions as you would like and implement the program in whatever way you would like.

There are several additional programs in the Github project for you to check out:
* `count.py` counts the number of occurrences of the word 'the'
* `sorter.py` is Spacco's standard _Ninja_ example that demonstrates how to create a class that can be sorted by one of its fields, similar to using Comparable in Java
* `test.py` demonstrates how to use random.choice() to randomly pick something from a list.

Commit your completed code to Github.

# Ngrams and Markov Chains

(This example is taken from [Andrew Cholakian's blog](http://blog.andrewvc.com/markov-http-benchmarking/))

To create a Markov Babbler, you need to process a text file N words at a time, producing a series of ngrams (the term _ngram_ is a generalization of the term _bigram_, which means two consecutive things).

If we are using an ngram size of 2, we will use 2 words of state and check all of the possible words that can follow each two words sequence.

So, after the first N words, what are all the possible words that can follow, and what are their probabilities?

The simplest case is where N=1, where we only use 1 word of state. Consider these sentences:

> I like cheese. I like butter. I don't like ham.

For this case, the word “I” is 2/3 likely to be followed by “like”, and 1/3 likely to be followed by “don’t”. We are processing two words at a time: One word of state and one word that can follow that state.

We can break this example into a Markov Chain state diagram that looks like this:

![Markov chain](http://blog.andrewvc.com/assets/images/chain.png)

We could convert this into a Python dictionary that looks something like this:

```python
{"I" => ["like", "don't"],
"don't" => ["like"],
"like" => ['cheese', 'ham', 'butter'],
"cheese" = ["."],
"ham" = ["."],
"butter" = ["."]}
```

Here are two more example sentences:

> mary had a little lamb . mary had a giant crab .

For ngrams where N=2 (i.e. a bigram), we could represent this in Python with a dictionary that looks something like this:

```python
{'mary had' => ['a'],
'had a' => ['little', 'giant'],
'a little' => ['lamb'],
'a giant' => ['crab'],
'little lamb' => ['.'],
'giant crab' => ['.']}
```

The state that we are using as keys in this dictionary are strings with spaces in between them, and the values are lists of words that could follow the keys. You will need to use string methods in Python to add and remove ngrams from the keys. You can also use _tuples_ to represent the state, although in Python tuples are immutable and need to be converted to a list, then modified and converted back.

When a period shows up as the next word, it means that we should end the current sentence, and randomly pick a new start state. This is why punctuation symbols are broken out separately in the test inputs.

You also need to track start states. In our example above, all sentences start with ‘mary had’. We know this because ‘mary had’ starts the input, and follows the period. We can track start states with a list.

Here is a diagram I found online for the ‘mary had a little lamb’ example:

![Mary had a little lamb](http://i.imgur.com/kCnOEiV.png)

To randomly choose something from a list in Python, try this:

```python
import random

mylist = ['dog', 'cat', 'dog', 'bird']
animal = random.choice(mylist)
print(animal)
```

This has a 1/2 chance of printing 'dog', and a 1/4 chance of printing either 'bird' or 'cat'.

You should test on a small input, not all of Shakespeare’s works.
Please test on something small to begin with, and make sure that your results make sense, before you work on something larger; otherwise it will be impossible to debug your program.
