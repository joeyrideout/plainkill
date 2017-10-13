ASCII_ALL = 128
ENGLISH_LETTER_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
        'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C':
        2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
        'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q':
        0.10, 'Z': 0.07}

def score_freq_ascii(frequencies):
    lang_dist = 0.0
    for i in range(65, 91):
        lang_dist += abs(frequencies[i] - ENGLISH_LETTER_FREQ[chr(i)])

    return lang_dist


def get_freq_ascii(message):
    counts = [0.0]*ASCII_ALL
    l = len(message)
    if l == 0:
        return counts

    for i in message:
        counts[ord(chr(str(i).upper()))] += 1

    # normalize and return frequencies
    return [x/l for x in counts]


def tests():
	#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]
    t1 = [0.0]*ASCII_ALL
    t1[97] = t1[98] = t1[99] = t1[100] = 0.25
    assert(get_freq_ascii("abcd") == t1)

    #>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
    t2 = [0.0]*ASCII_ALL
    t2[97] = 0.5
    t2[98] = 0.0
    t2[99] = t2[100] = 0.25
    assert(get_freq_ascii("adca") == t2)

    #>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
    assert(get_freq_ascii('bewarethebunnies')[97] == 0.0625)

    passage = "Father Zossima, lifting his eyes, looked at him, and said with a smile:  1cYou have known for a long time what you must do. You have sense enough: don 19t give way to drunkenness and incontinence of speech; don't give way to sensual lust; and, above all, to the love of money. And close your taverns. If you can 19t close all, at least two or three. And, above all- don't lie."
    print score_freq_ascii(get_freq_ascii(passage))

tests()
