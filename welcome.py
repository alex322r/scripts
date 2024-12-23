#Display welcome message and info

# get linux os username
import os
from PIL import Image

SYSTEM_USER = os.getenv('USER')

WELCOME_MESSAGE = f"Welcome back {SYSTEM_USER}! \n"
WELCOME_IMAGE = f"/home/{SYSTEM_USER}/Imágenes/takagi.png"

def resize_welcome_image(width=75, height=150):
    try:
        # Open original image
        with Image.open(WELCOME_IMAGE) as img:
            # Resize with antialiasing
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
            # Save resized image
            output_path = WELCOME_IMAGE.replace('.png', '_resized.png')
            resized_img.save(output_path)
            return output_path
    except Exception as e:
        print(f"Error resizing image: {e}")
        return WELCOME_IMAGE

# Update welcome image path to use resized version
WELCOME_IMAGE = resize_welcome_image()

def welcome():
    # check if command kitty is installed
    try:
        import os
        # display image using kitty rezise image to fit terminal
        os.system("kitty icat --align left --place 75x150@2x1 " + WELCOME_IMAGE)
        os.system("echo " + WELCOME_MESSAGE)
    except:
        print("kitty is not installed, please install kitty to display image")

welcome()