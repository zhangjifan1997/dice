def name_input(question):
    string=raw_input(question)
    if len(string)>10:
        string=string[0:9]
        print "the name is too long. I'll give you a nickname."
    return string

def int_input(question):
    number=raw_input(question)
    try:
        number=int(number)
    except:
        number=int_input(question)
    return number

def float_input(question):
    number=raw_input(question)
    try:
        number=float(number)
    except:
        number=float_input(question)
    return number
