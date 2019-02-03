import os
import sys
import re

subs = {}
pattern = r"\d\d[xe]\d\d"

try:
    for filename in os.listdir(sys.argv[1]):
        #group files with similar numbers
        match = re.findall(pattern, filename)
        if match:
            sub_key = "".join(re.split(r"\D", match[0])) # 01x07 and 01e07 -> 0107
            if sub_key in subs.keys():
                subs[sub_key].append(filename)
            else:
                subs[sub_key] = [filename]
        # analyze the groups for .srt and .avi files
    for filegroup in subs.values():
        if(len(filegroup) != 2):
            print("You have to do it manually, there are several subs for one video.")
            break
        else:
            for filename in filegroup:
                # rename the subs as the videofile
                if filename.endswith(".srt") or filename.endswith(".ass"):
                    to_rename = filename
                elif filename.endswith(".avi") or filename.endswith(".mp4"):
                    video_file = filename
            path_to_rename = os.path.join(sys.argv[1], to_rename)
            path_new = os.path.join(sys.argv[1], video_file[:-4] + ".srt")
            print(path_to_rename)
            print(path_new)
            os.rename(path_to_rename, path_new)

except IndexError:
    print("Define the folder in which to rename subtitles.")
    print("Syntax: rename-subs [folder path]")
