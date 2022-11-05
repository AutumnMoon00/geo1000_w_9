def sed(pat_str, rep_str, file1, file2="outfile.txt"):
    try:
        with open(file1, 'r') as fin:
            text = fin.readlines()
            print(type(text))
            text_new = [line.replace(pat_str, rep_str) for line in text]
            print('all good')
            # new_text = text.replace(pat_str, rep_str)

        f_out = open(file2, 'w')
        print("all good 2")
        # f_out.write(text_new)
        for line in text_new:
            f_out.write(line)
        print("all good 3")
        f_out.close()

    except:
        print("there's something wrong")


sed('And', 'Or', "mr_brightside_lyrics.txt")