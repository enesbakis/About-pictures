from PIL import Image
import glob, os
import sys



size = 128, 128

for infile in glob.glob(sys.argv[1]):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "JPEG")