while True:
    try:
        a = input()
        print(a)

    # Runtime Error 발생시 break!!!!
    except EOFError:
        break