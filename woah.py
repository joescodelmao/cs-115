def leppard(input_string):
    output_string = ''
    for symbol in input_string:
        if symbol == 'o':
            output_string = output_string + 'ooo'
        else:
            output_string = output_string + symbol
    return output_string
vowles = ['a', 'e', 'i', 'o', 'u']
def spamify(word):
    for i in range(len(word)):
        if word[i] not in vowles:
            return word [0:i] + 'spam' + word[i+1:]
        return word
def fact(r1):
    r13 = 1
    while r1 !=0:
        r13 *=r1
        r1 -= 1
    return r13
