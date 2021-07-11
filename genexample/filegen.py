import os

root = "music"

for path, downloads, music in os.walk(root, topdown=True):
    print(path)
    for f in music:
        print("\t{}".format(f))