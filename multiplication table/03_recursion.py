def multable(num, i):

    if i > 10:
        # return means: Exit the function now.
        return

    print(i, "x", num, "x", num * i)
    multable(num, i + 1)


multable(5, 1)
