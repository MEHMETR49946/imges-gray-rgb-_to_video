import glob
from moviepy.editor import ImageClip, concatenate_videoclips
from PIL import Image


def convert_to_rgb(image_file_name):
    img = Image.open(image_file_name)
    if img.mode != "RGB":
        img = Image.open(image_file_name).convert('RGB')
        img.save(image_file_name)
        


class VideoFile:
    def __init__(self, fname):
        self.fname = fname
        self.clips = []


    def add_image_directory(self, dirname, ext="png"):
        files = glob.glob(f"{dirname}/*.{ext}")
        for fname in files:
            self.add_image(fname)

    def add_image(self, image_file_name):
        convert_to_rgb(image_file_name)
        self.clips.append(ImageClip(image_file_name).set_duration(1))

    def save(self,  fps=24, method="compose"):
        temp = concatenate_videoclips(self.clips, method = method)
        temp.write_videofile(self.fname, fps=fps) 
        
