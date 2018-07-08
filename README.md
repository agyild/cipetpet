# cipetpet
A text (de)obfuscator based on Turkish language game "kuş dili".
## Usage
```
>cipepet.py -h
usage: cipetpet.py [-h] (-O | -D) [-c C] [-rc {0,1,2}] [-r N] [-rr]
                   text [text ...]

positional arguments:
  text                  Text to be (de)obfuscated.

optional arguments:
  -h, --help            show this help message and exit

actions:
  -O, --obfuscate       Convert text to kus dili.
  -D, --deobfuscate     Convert text back to Turkish.

obfuscate options:
  -c C, --consonant C   A consanant to be used during syllable generation.
  -rc {0,1,2}, --random-consonant {0,1,2}
                        Consonant randomization level.
  -r N, --repeat-syllable N
                        How many times to repeat kus dili syllables at
                        maximum.
  -rr, --random-repeat-syllable
                        If set, syllable repetitions are randomized between 1
                        and --repeat-syllable value.
```
### Example
```
>cipetpet.py -O "Pijamalı hasta yağız şoföre çabucak güvendi."
Pigijagamagalıgı hagastaga yagağıgız şogofögörege çagabugucagak gügüvegendigi.
>cipetpet.py -O "Pijamalı hasta yağız şoföre çabucak güvendi." -rc 2 -r 42 -rr
Pijijijijijijijijajajajajajajajajajajajajajajajajajajajajajajajajajajajajajamajajajajajajajajajajajajajajalıjıjıjıjıjıjıjıjıjıjıjıjıjıjıjıjı hamamamamamamastamamamamamamamamamamamamamamamamamamamamamamama yaçaçağıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçıçız şoboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboboföböböböböböböböböböböböböböböböböböböböböböböböböböböböböböböböbörebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebe çatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatabutututututututututututututututututututututututututututututucatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatatak gühühühühühühühühühühühüvehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehendihihihihihihi.
>cipetpet.py -D "Pififififijafafafafafafafafafafafafafafafafafafafafafafafafafafafafafamafafafafafafafalıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfı hafafafafafafafastafafafafafafafafafafafafafafafafafafafafafafafafafafafafa yafafafafafafafafafafafafafafafafafafafafafafafafafafafafafağıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfıfız şofofofofofofoföföföföföföföföföföföföföförefefefefefefefefefefefefefefefefefefefefefefefe çafafafafafafafafafafafafafafafafafafafafafafafafafafabufufufufufufufufufucafafafafafafafafafafafafafafak güfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüfüvefefefefefefendifififi."
Pijamalı hasta yağız şoföre çabucak güvendi.
```
## Known Issues
* Piping output does not work correctly at the moment (at least in Windows). Pipe and redirection characters cause a glitch in Python's Unicode mapping mechanism. Will need to do more research to implement a workaround.
* With consonant randomization level 2 and randomized syllable repetition deobfuscation might guess a single or few syllables wrong. Will try to replace current regex pattern with a less error-prone one.
