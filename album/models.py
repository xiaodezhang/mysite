from django.db import models
from PIL import Image

# Create your models here.

# import my imgs script
def import_exist_imgs(path):
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            img = Image.open(file)
##            if img.format.isimg: 
                create all types we need,including thumbnail,small...
#                # add to database
                
            files.append(os.path.join(r,file))

# check all these imgs existe before the server start.
def check_imgs_exist():
    files = get_all_files() # from database
    try:
    for file 
    except:
        print("open files failed")



class Img(models.Model):
    name = models.CharField(max_length=256)
    type = models.charField(max_length=20) #origin,thumbnail,small,medium,large



test pillow
from PIL import Image

size = (128,128)
try:
    img = Image.open("test.JPG")
    img.thumbnail(size)
    img.save("test_thumbnail.JPG","JPEG")
    print(img.format,img.size,img.mode)
except IOError:
    print("cannot create thumbnail")
