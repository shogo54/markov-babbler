# Markov Babbler

This was a class assignment for CS 317 (Artificial Intelligence) in the Fall term in 2017 at Knox College. 
I built a “Markov Babbler” that uses [Markov Chains](https://en.wikipedia.org/wiki/Markov_chain) to “babble” random sentences.

I trained our babbler on a large amount of text (usually called a _corpus_), and then have it generate random sentences that sound vaguely like they were written by the same author as the training set.

**Note** Don’t train the babbler on racist tweets or it could end up sounding like Microsoft’s now-defunct [Nazi-sympathizing, Holocaust-denying Twitter-bot Tay](http://theantimedia.org/microsofts-new-twitter-bot-becomes-nazi-sympathizing-maniac-within-24-hours/), which probably used something like Markov Chains in its implementation.

The complete works of Shakespeare is available [in a huge text file here](https://drive.google.com/open?id=0B8YG7KPaRWn7bXEwUDlOSEV6QXc) (only visible on campus), or you can use any large amount of text you are interested in. 
[Project Gutenberg](http://www.gutenberg.org/) online has a ton of this sort of thing available, although you will have to process it somewhat to get it into the right format by breaking out all of the punctuation.

The starter Python program is `markovbabbler.py`. 
There are several additional programs in the Github project for you to check out:
* `count.py` counts the number of occurrences of the word 'the'

## Ngrams and Markov Chains

(This example is taken from [Andrew Cholakian's blog](http://blog.andrewvc.com/markov-http-benchmarking/))

this Markov Babbler processes a text file N words at a time, producing a series of ngrams (the term _ngram_ is a generalization of the term _bigram_, which means two consecutive things).

If the program is using an ngram size of 2, the babbler will use 2 words of state and check all of the possible words that can follow each two words sequence.

The simplest example is where N=1, where the program only uses 1 word of state. 
Consider these sentences:

> I like cheese. I like butter. I don't like ham.

For this case, the word “I” is 2/3 likely to be followed by “like”, and 1/3 likely to be followed by “don’t”. 
The program is processing two words at a time: One word of state and one word that can follow that state.

This example can be broken into a Markov Chain state diagram that looks like this:

![Markov chain](http://blog.andrewvc.com/assets/images/chain.png)

The program converts this into a Python dictionary that looks like this:

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

For ngrams where N=2 (i.e. a bigram), the representation of this in Python with a dictionary looks something like this:

```python
{'mary had' => ['a'],
'had a' => ['little', 'giant'],
'a little' => ['lamb'],
'a giant' => ['crab'],
'little lamb' => ['.'],
'giant crab' => ['.']}
```

The state used as keys in this dictionary are strings with spaces in between them, and the values are lists of words that could follow the keys.

When a period shows up as the next word, it means that the program ends the current sentence, and randomly pick a new start state.
This is why punctuation symbols are broken out separately in the test inputs.

The program also keeps track of start states. 
In the example above, all sentences start with ‘mary had’. 

The below is a diagram for the ‘mary had a little lamb’ example:

![Mary had a little lamb](http://i.imgur.com/kCnOEiV.png)
