fout = open('output_v1.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
# line2 = "the emblem of our land.\n"
# fout.write(line2)

camels = 42
line3 = "I've spotted %d camels" % camels
fout.write(line3)

fout.close()
