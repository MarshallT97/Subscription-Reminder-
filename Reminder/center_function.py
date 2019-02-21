def center(width, height, base):
    # sw,sh holds the system screen width/height
    sw = base.winfo_screenwidth()
    sh = base.winfo_screenheight()
    # x,y set up the starting position of the window
    x = (sw - width) / 2
    y = (sh - height) / 2
    # set up the size of the window
    base.geometry('{}x{}+{}+{}'.format(width, height, int(x), int(y)))