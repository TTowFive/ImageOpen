from PIL import Image
import sys

try:
    User_index_image_file = sys.argv[1] #获取用户想要打开的图片路径
except:
    print ( "Error! \n"
            "Form: ImageOpen [You Want To open image]" )
    sys.exit()
im = Image.open( User_index_image_file,"r" )

im.show()