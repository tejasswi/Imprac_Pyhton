import sys
def load(palingrams):
    #Open a text fiel&return list of lower string
    try:
        with open(palingrams) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\n Error opening {}.Terminatinf program.".format(e,file), file = sys.stderr)
        sys.exit(1)