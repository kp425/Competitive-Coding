
def number_of_vowels(my_string):

    vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]


def reverse(my_string):
    s = " "
    for i in my_string[::-1]:
        s+= i
    return s

def reverse_order(my_string):

    s = " "
    for i in my_string.split(" ")[::-1]:
        s+= i+" "
    return s

def rotate(s1, s2, no_of_chars):

    return s1[-1*no_of_chars:] + s1[:-1*no_of_chars] == s2









if __name__ == "__main__":

    my_string = "my name is uchiha Madara"

    print(reverse_order(my_string))

    print(rotate("ABCD", "CDAB",2))


