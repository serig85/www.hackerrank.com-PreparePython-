def mutate_string(string, position, character):
    #V1
    #l = list(string)
    #l[position] = character
    #string = ''.join(l)
    #V2
    string = string[:position] + character + string[position+1:]

    return string

