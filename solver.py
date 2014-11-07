import sys
import copy

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHADICT = {
     'a' : 0,
     'b' : 0,
     'c' : 0,
     'd' : 0,
     'e' : 0,
     'f' : 0,
     'g' : 0,
     'h' : 0,
     'i' : 0,
     'j' : 0,
     'k' : 0,
     'l' : 0,
     'm' : 0,
     'n' : 0,
     'o' : 0,
     'p' : 0,
     'q' : 0,
     'r' : 0,
     's' : 0,
     't' : 0,
     'u' : 0,
     'v' : 0,
     'w' : 0,
     'x' : 0,
     'y' : 0,
     'z' : 0 }

BY_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def main():
    # open file provided as argument
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        fl = list(f)
    else:
        sys.exit("usage: python solver.py filename.txt")

    # determine frequency of each letter in the file
    freq_dict = letter_freq_file(fl)

    #create alphabet sorted by frequency of occurence in the file.
    alphabet_by_freq = sorted(freq_dict,
                              key = lambda x: freq_dict[x],
                              reverse=True)

    # print substituted version of the file
    for line in fl:
        print(substitute(line, alphabet_by_freq))

def letter_freq(s, freq_dict):
    for letter in s:
        if letter.lower() in ALPHABET:
            freq_dict[letter.lower()] += 1

def letter_freq_file(string_list):
    freq_dict = copy.deepcopy(ALPHADICT)
    for s in string_list:
        letter_freq(s, freq_dict)

    return freq_dict

def alpha_position(letter):
    return ALPHABET.index(letter.lower()) + 1

def substitute(string, alphabet_by_freq):
    ret = ''
    for letter in string:
        if letter.lower() in ALPHABET:
            ret += alphabet_by_freq[alpha_position(letter)-1]
        else:
            ret += letter
    return ret

main()
