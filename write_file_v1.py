fout = open('output_v1.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)

camels = 42
line3 = "I've spotted %d camels\n" % camels
fout.write(line3)

line4 = "In %d years I've spotted %g %s." % (3, 0.1, 'camels')
fout.write(line4)

fout.close()
