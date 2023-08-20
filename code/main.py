import os


path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(path)
files.remove("main.py")
print(files)

for index, file in enumerate(files):
    os.rename(
        os.path.join(path, file), os.path.join(path, "img_100000_{}.jpg".format(index))
    )
