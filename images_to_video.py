import os
from moviepy.editor import *
from PIL import Image
import cv2
blue_dot = Image.open(os.path.join(os.getcwd(), "mavi_nokta.png"))
blue_dot = blue_dot.resize((1,1)) # nokta şeklinde
os.chdir("slides")
slides = [file for file in os.listdir(".") if file.endswith(".png")]
for img in slides:
    img_name = img
    img = Image.open(img)
    dst = Image.new("RGB", (img.width, img.height))
    dst.paste(img, (0,0))
    dst.paste(blue_dot, (0,0))
    dst.save(img_name)


clips = []
for img in slides:
    clips.append(ImageClip(img).set_duration(1))

video = concatenate_videoclips(clips, method="compose")
video.write_videofile("video.mp4", fps=24)