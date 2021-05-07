#!/usr/bin/python3
def multiple_returns(sentence):
    letter = None
    if sentence:
        letter = sentence[0]
    num = len(sentence)
    return(num, letter)
