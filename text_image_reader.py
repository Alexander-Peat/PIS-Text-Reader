file = open(r"C:\Users\ajpea\My Folders\Image Reader\.pis (Peat Image Standard) Files\buran.pis", "r")

string = file.read()
colours = string.split(";")
b_w = [0] * 10000

for loop in range(len(colours) - 1):
    ind_colours = colours[loop].split(",")
    #print(ind_colours)
    r = int(ind_colours[0])
    g = int(ind_colours[1])
    b = int(ind_colours[2])

    avg = round(((r + b + g) / 3), 0)
    b_w[loop] = avg

counter = 0
line = ""
for loop in range(10000):
    if b_w[loop] < 85:
        char = "."
    elif b_w[loop] < 170:
        char = "o"
    else:
        char = "@"
        
    line = line + char + " "
    counter = counter + 1

    if counter == 100:
        counter = 0
        print(line)
        line = ""
