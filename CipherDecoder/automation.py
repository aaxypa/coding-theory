# Get a data structure containing a few hundred English words.
from english_words import english_words_set
from m2 import decode, encode

def evaluateShift(string):
    eval = 0
    to_Shift = None
    for i in range(25):
        text = decode(string, i)
        # Use dictionary
        words = text.split(" ")
        count = 0
        for text in words:
            if text in english_words_set:
                count += 1
        if count > eval:
            eval = count
            to_Shift = i

    print(f"{to_Shift} letter shift: {decode(string, to_Shift)}")

    return to_Shift

if __name__ == '__main__':
    evaluateShift("ywnfslqj")
    evaluateShift("juu axjmb unjm cx axvn")
    evaluateShift("x lpccp qt pc tmrtaatci rdstg")