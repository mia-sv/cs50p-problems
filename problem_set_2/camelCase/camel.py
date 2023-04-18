def main():
    camelcase = input("camelcase: ")
    print(snakecase(camelcase))



def snakecase(word):
    i = 0
    new_word = word

    while i < len(new_word):
        if new_word[i].isupper():
           part_1 = new_word[0:i]
           part_2 = new_word[i].lower()
           part_3 = new_word[i+1:len(new_word)]
           new_word = part_1 + "_" + part_2 + part_3
           i = i + 1

        i = i + 1

    return new_word


    
    

main()