import os
import glob
import base64
# import argparse

py_path = os.path.abspath(__file__)
py_dir = os.path.dirname(py_path)
os.chdir(py_dir + "/svgs/")


def cap(file=''):
    side = abs(50 - len(file))//2
    if len(file) > 0:
        return "<" + "="*side + file + "="*side + ">" + "\n"
    return "\n" + "<" + "="*side + file + "="*side + ">" + "\n"*2


img_dict = {}

for file in glob.glob("*.svg"):
    with open(file, "rb") as image:
        img_dict[file] = "data:image/svg+xml;charset=utf-8;base64, " + \
            base64.b64encode(image.read()).decode("utf-8")

os.chdir(py_dir)
with open("svgs_b64_encoded_output.txt", 'w') as f:
    for file, image in img_dict.items():
        f.write(cap(file))
        f.write(image)
        f.write(cap())
