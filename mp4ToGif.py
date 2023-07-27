from moviepy.editor import *
import os

def convert_mp4_to_gif(input_file, output_file):
    clip = VideoFileClip(input_file)
    print(clip.duration)
    clip = clip.fx(vfx.speedx,clip.duration)
    clip.write_gif(output_file)

if __name__ == "__main__":
    # input_file = "Media/mp4/Alvin Dance.mp4"  # Replace with the path to your input MP4 file
    # output_file = "Media/gif/Alvin Dance.gif"  # Replace with the desired output GIF file name

    # Optional: If you want to convert only a specific duration of the video, set the 'duration' parameter (in seconds)
    # duration = 10
    
    convert_mp4_to_gif(r"D:\YD\50k.mp4", 'Media/YD50k.gif')
    convert_mp4_to_gif(r"D:\YD\Final.mp4", 'Media/YD100k.gif')
    # for Video in os.listdir('Media/mp4/'): 
    #     convert_mp4_to_gif('Media/mp4/'+Video, 'Media/gif/'+Video.replace('.mp4','.gif'))
