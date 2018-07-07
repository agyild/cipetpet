"""
This module which consists of a single class and Turkish alphabet related
constants is used by the cipetpet front-end. It also can be imported into
other projects if desired.
"""

import random
import re

_VOWELS = 'aeıioöuü' + 'âîû'
_CONSONANTS = 'bcçdfgğhjklmnprsştvyz'


class KusDili:
    def __init__(self, *text):
        """
        A generic KusDili object constructor that accepts the common
        variables used by both obfuscation and deobfuscation procedures.
        
        :param str text: A string object to be (de)obfuscated that is at
            least 1 character long.
        """

        if not all(isinstance(_, str) for _ in text):
            raise TypeError('text(s) has to be a str object.')
        else:
            if any(len(_) < 1 for _ in text):
                raise ValueError(
                    'text(s) has to be at least 1 character long.')

        self.text = text
        self.processed_text = []

        self.random_consonant = None
        self.consonant = None

    def obfuscate(self, consonant='g', random_consonant=0, repeat_syllable=1,
                  random_repeat_syllable=False):
        """
        Obfuscates/translates to kuş dili the given text(s).
        
        By default a predefined static consonant is used for syllable
        generation, in addition random_consonant might be set for random
        consonant generation.
        
        :param str consonant: (optional) A 1 character long consonant to be
            used during syllable generation. Default is 'g'.
        :param int random_consonant: (optional) A numeric value between 0
            and 3 (inclusive) which determines the randomness
            characteristics of the consonant. For the values 1, 2 and higher
            than 3 the consonant is generated on per-text, per-word or
            per-syllable basis.
        :param int repeat_syllable: (optional) A numeric value higher than 1
            which determines how many times to repeat the kuş dili syllables.
        :param bool random_repeat_syllable: (optional) A boolean value which
            determines if the syllable repetitions are randomized or not. If
            True, for each word random length of repetitions occur such that 1
            <= repeat <= repeat_syllable. Default is False.
        :return: Obfuscated text(s) with the type determined according to
            the amount of input text(s).
        :rtype: str or list
        """

        if not isinstance(consonant, str):
            raise TypeError('key has to be a str object.')
        else:
            if len(consonant) != 1:
                raise ValueError('key has to be at least 1 character long.')
            elif consonant.lower() not in _CONSONANTS:
                raise ValueError('key has to be a valid consonant.')

        self.consonant = consonant.lower()
        self.random_consonant = int(random_consonant)

        _regex = re.compile(r'[{}]'.format(_VOWELS), re.I)

        def _word_processor():
            """
            Helper generator function that sends the words from the
            enclosing scope alongside with any spaces or punctuation
            characters next to them to the inner _syllable_processor helper
            function.
            
            :return: Obfuscated word in kuş dili.
            :rtype: str
            """

            def _syllable_processor(block):
                """
                Sub-helper function that processes the syllables and makes sure
                that they are obfuscated in a way that is consistent with
                the current word structure.
                
                :param re.__Match[T] block: A syllable or vowel block that
                    is constructed by the re.sub method.
                :return: A processed syllable or vowel block.
                :rtype: str
                """

                syllable = ''

                for syllable_repetition in range(
                        repeat_syllable if not random_repeat_syllable
                        else random.randint(1, repeat_syllable)):
                    if self.random_consonant > 2:
                        self.consonant = random.choice(_CONSONANTS)
                    _syllable = self.consonant
                    if word.isupper():
                        _syllable = _syllable.upper()
                    _syllable += block[0].lower() if word.istitle() else (
                        block[0])

                    syllable += _syllable

                return block[0] + syllable

            for word in re.findall(r'\s*\S+\s*', text):
                if self.random_consonant == 2:
                    self.consonant = random.choice(_CONSONANTS)
                yield _regex.sub(_syllable_processor, word)

        for text in self.text:
            if self.random_consonant == 1:
                self.consonant = random.choice(_CONSONANTS)
            self.processed_text.append(''.join(_word_processor()))

        self._trim()
        return self.__repr__()

    def deobfuscate(self):
        """
        Deobfuscates/translates back to Turkish the given kuş dili text(s).

        :return: Obfuscated text(s) with the type determined according to
            the amount of input text(s).
        :rtype: str or list
        """

        _regex_rep = re.compile(
            r'([{}][{}])?(\1)+'.format(_CONSONANTS, _VOWELS), re.I)
        _regex_syl = re.compile(
            r'([{}])[{}]\1'.format(_VOWELS, _CONSONANTS), re.I)

        for text in self.text:
            text = _regex_syl.sub(r'\g<1>', _regex_rep.sub(r'\g<1>', text))

            # Python 3.6.1 has a bug that generates extra U+0307 characters
            # when processing Turkish vowels 'iİ', as a temporary fix we
            # replace these characters with an empty char
            # See: https://bugs.python.org/issue17252
            self.processed_text.append(text.replace('\u0307', ''))

        self._trim()
        return self.__repr__()

    def _trim(self):
        if len(self.processed_text) == 1:
            self.processed_text = self.processed_text[0]

    def __repr__(self):
        return self.processed_text if self.processed_text else None
