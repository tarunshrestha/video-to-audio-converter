import os
import moviepy.editor
from tkinter.filedialog import *


def main():
    canplay = True
    while canplay:
        os.system('cls')
        vids = askopenfilenames()
        for i in vids:
            video = moviepy.editor.VideoFileClip(i)
            aud = video.audio
            name = input(f"Name the Audio for {os.path.basename(i)}:")
            #output_directory = "\\Audio\\"
            #os.makedirs(output_directory, exist_ok=True)
            aud.write_audiofile(f"{name}.mp3")
        print("Successfully converted all videos to audio!")
        canplay = False
        exit()
        # ask = input("Do you wanna convert again?Type 'y' or 'n'.\n").lower()
        # if ask != "y":
        #     print("GoodBye!")
        #     canplay = False
        # else:
        #     main()


main()

