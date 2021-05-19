def pattern():

    sentence = input("Please enter a sentence : ")

    while True:
        try:
            waves_num = int(
                input("Please enter the number of waves you would like : "))

            extend = int(
                input("Enter the max spaces (width) of the wave : ")) * 2

        except ValueError:
            print("Please enter a valid input")
            continue

        list_con = list(sentence)
        for i in range(1, waves_num+1):
            for j in range(1, extend):
                if j <= int(extend/2):
                    list_con.insert(0, " ")
                    print(''.join(list_con))
                else:
                    del list_con[0]
                    print(''.join(list_con))

        break

    while True:
        p_again = input("Do you want to make it again?(Y/N) :")
        if p_again.lower() in 'yn':
            if p_again.upper() == "Y":
                pattern()

        else:
            print("Please enter a valid input (Y/N)")
            continue

        break


pattern()
