import random
import subprocess

def main():

    again = 'y'
    word_dict = {}

    title = input("enter the name of a video (hit enter to quit): ")

    while again == 'y' or again == 'Y':

        word_list = []
        titleWords = title.split()
                        
        for word in titleWords:
            word_list.append(word + " ")

        word_dict = dictionary(word_list, word_dict)

        title = input("enter the name of a video (hit enter to quit): ")

        if title == '' :
            again = 'n'

    word = random.choice(list(word_dict.keys()))
    while word != "EOL ":
        print(word, end='')
        word = random.choice(word_dict[word])


def dictionary(list, word_dict):

    list.append("EOL ")

    idx = 0
    for word in list[:-1]:
        if word in word_dict:
            word_dict[word].append(list[idx+1])
        else:
            word_dict[word] = [list[idx+1]]
        idx += 1

    return word_dict

main()
