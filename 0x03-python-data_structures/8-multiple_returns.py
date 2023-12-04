#!/usr/bin/python3
def multiple_returns(sentence):
    for item in sentence:
        if len(sentence) != 0:
            result = tuple((len(sentence), sentence[0]))
            return result
        else:
            return None

