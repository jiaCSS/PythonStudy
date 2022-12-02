def get_name():
    with open("name.txt", mode = "r") as n:
        name_list = []
        for line in n:
            
            x =  ' '.join( line.split())
            name_list.append(x)
        print(name_list)
        return name_list
    
namelist = get_name()


for index in range(len(namelist)):
    with open("starting_letter.txt", mode = "r") as s:
        search_text = "name"
        data = s.read()
        print(data)
        data_replace = data.replace(search_text, namelist[index])
        print(data_replace)

    with open(f"./readyToSend/{namelist[index]}.txt", mode = "w") as replace_word:
        replace_word.write(data_replace)


