def exercise_3(inputs): # DO NOT CHANGE THIS LINE
    import Exercise_3_library

    while True:
        a=input("Input a sentence (input 'stop' to end) : ")

        if a!="stop":
            Exercise_3_library.sorter(a)
            Exercise_3_library.counter(a)
            Exercise_3_library.finder1(a)
            Exercise_3_library.finder2(a)

        elif a=="stop":
            break
            
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
