#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)

    if x == 0:
        return (x, None)
    return(x, sentence[0])
