import os

output_file = 'path/to/downloaded_video'
channels = open('path/to/video_urls', 'r', encoding='latin-1').readlines()

count = 0
for i in channels:
    if i == '\n':
        continue
    cmd = 'yt-dlp -i --no-warnings '
    cmd = cmd + '-c '  # resume download, in case it got stopped
    cmd = cmd + '--no-overwrites '
    cmd = cmd + '--write-description '  # description file may contain movie name
    cmd = cmd + '--write-auto-subs ' # save automatically generated subtitles
    cmd = cmd + '--write-sub ' # save subtitles
    cmd = cmd + "--sub-langs en.* " #optional, specific only download subtitles in certain languages
    cmd = cmd + "-o " + output_file + "/%(id)s.%(ext)s " # output path and output format
    cmd = cmd + i
    os.system(cmd)

