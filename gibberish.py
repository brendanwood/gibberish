#!/usr/bin/env python
import string
import random

__all__ = ('generate_word', 'generate_words')

initial_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                      # remove those easily confused with others
                      - set('qxc')
                      # add some crunchy clusters
                      | set(['bl', 'br', 'cl', 'cr', 'dr', 'fl',
                             'fr', 'gl', 'gr', 'pl', 'pr', 'sk',
                             'sl', 'sm', 'sn', 'sp', 'st', 'str',
                             'sw', 'tr', 'ch', 'sh'])
                      )

final_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                    # remove the confusables
                    - set('qxcsj')
                    # crunchy clusters
                    | set(['ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt',
                           'pt', 'sk', 'sp', 'ss', 'st', 'ch', 'sh'])
                    )

vowels = 'aeiou'

prefixes = (
    'an', 'anti', 'ante', 'auto', 'circum', 'co', 'com', 'con', 'contra', 'de', 'dis',
    'en', 'ex', 'extra', 'hetero', 'homo', 'hyper', 'in', 'inter', 'intra', 'macro',
    'micro', 'mono', 'non', 'omni', 'post', 'pre', 'pro', 'sub', 'trans', 'tri', 'un', 'uni',
)

suffixes = (
    'acy', 'al', 'ance', 'ence', 'dom', 'er', 'or', 'ism', 'ist', 'ity', 'ment',
    'ness', 'ship', 'sion', 'tion', 'ate', 'en', 'ify', 'ize', 'ise', 'able', 'ible',
    'al', 'esque', 'ful', 'ic', 'ical', 'ious', 'ous', 'ish', 'ive', 'less', 'y',
    'ed', 'ing',
)

prefix_odds = 0.7
suffix_odds = 0.7

def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word."""
    word = ''.join(random.choice(s) for s in (initial_consonants,
                                              vowels,
                                              final_consonants))
    if random.random() < prefix_odds:
        word = random.choice(prefixes) + word
    if random.random() < suffix_odds:
        word = word + random.choice(suffixes)
    return word


def generate_words(wordcount):
    """Returns a list of ``wordcount`` pseudo-words."""
    return [generate_word() for _ in xrange(wordcount)]


def console_main():
    import sys
    try:
        wordcount = int(sys.argv[1])
    except (IndexError, ValueError):
        wordcount = 1
    print(' '.join(generate_words(wordcount)))


if __name__ == '__main__':
    console_main()
