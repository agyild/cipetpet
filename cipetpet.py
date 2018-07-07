#!/usr/bin/env python3

import argparse

from lib import cipetpet

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser_actions = parser.add_argument_group(title='actions')
    parser_actions_ex = parser_actions.add_mutually_exclusive_group(required=True)
    parser_actions_ex.add_argument('-O', '--obfuscate', action='store_true', help='Convert text to kus dili.')
    parser_actions_ex.add_argument('-D', '--deobfuscate', action='store_false', dest='obfuscate', help='Convert text back to Turkish.')
    parser_obfuscate = parser.add_argument_group(title='obfuscate options')
    parser_obfuscate.add_argument('-c', '--consonant', default='g', type=str, help='A consanant to be used during syllable generation.', metavar='C')
    parser_obfuscate.add_argument('-rc', '--random-consonant', default=0, type=int, choices=[0, 1, 2], help='Consonant randomization level.')
    parser_obfuscate.add_argument('-r', '--repeat-syllable', default=1, type=int, help='How many times to repeat kus dili syllables at maximum.', metavar='N')
    parser_obfuscate.add_argument('-rr', '--random-repeat-syllable', action='store_true', help='If set, syllable repetitions are randomized between 1 and --repeat-syllable value.')
    parser.add_argument('text', nargs='+', type=str, help='Text to be (de)obfuscated.')
    args = parser.parse_args()

    kusdili_job = cipetpet.KusDili(*args.text)

    if args.obfuscate:
        result = kusdili_job.obfuscate(args.consonant, args.random_consonant, args.repeat_syllable, args.random_repeat_syllable)
    elif not args.obfuscate:
        result = kusdili_job.deobfuscate()

    if isinstance(result, str):
        print(result)
    elif isinstance(result, list):
        for _result in result:
            print(_result)

    # met = 'Pijamalı hasta yağız şoföre çabucak güvendi.'
    # foo = cipetpet.KusDili(met)
    # foo.obfuscate(random_consonant=2, repeat_syllable=3, random_repeat_syllable=True)
    # print(foo)