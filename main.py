from PIL import Image, ImageDraw
import os

start_x = 10
start_y = 10
end_x = 10
end_y = 10
spacing_each_row = 10
line_color = (100,100,100,128)
line_width = 5

for f in os.listdir("./Original"):
    # Open
    im = Image.open(f'./Original/{f}')
    image_width,image_height = im.size

    # Draw
    draw = ImageDraw.Draw(im)
    # For loop change y value, check y value more than (height-end_y)
    for height in range(start_y,image_height,spacing_each_row):
        draw.line((start_x,height,image_width-end_x,height),fill=line_color,width=line_width)

    # Save
    fn,fext = os.path.splitext(f)
    im.save(f"./Edited/Edited_{fn}.jpg","JPEG")
