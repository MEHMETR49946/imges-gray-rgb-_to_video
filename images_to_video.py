from video import VideoFile

v = VideoFile("test.mp4")
v.add_image_directory("slides")
v.save()

