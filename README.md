
# Multilingual-SyMoN
## Dataset release
Here we release a video-language story dataset, M-SyMoN, which consist of 13,166 video summaries of popluar movies and TV shows in 7 languages (English, Chinese, Spanish, Portugese, French, Hindi, Russian). M-SyMoN is subitable for a varity of multilingual video story understanding tasks such as video-text retrieval, video temporal ordering, video-text alignment, etc. We release M-SyMoN for research purposes, please contact us if you would like to use the dataset of other purposes.

## Introduction
This dataset contains 13,166 movie/TV-show summary videos from various Youtube channels. You can find the download instructions and annotation file explainations here:

### Download
The video urls for the unsupervised portion of M-SyMoN is stored in: `url list of unsupervised videos/`

The video urls for the videos annotated portion of M-SyMoN is stored in: `url list of annotated videos/`

#### Install yt-dlp (https://github.com/yt-dlp/yt-dlp) for downloading videos from Youtube 
`python3 -m pip install -U yt-dlp`

#### Use yt-dlp to download videos from url_list
`yt-dlp -i --no-warnings -c --no-overwrites --write-description --write-auto-subs --write-sub --sub-langs [target_language].* -o [output_dir]/%(id)s.%(ext)s --batch-file path/to/url_list.txt`

[output_dir] is the output directory you wish to save the videos to.

[target_language] specifies the language of the subtitles.

### Annotation
We annotate 480 videos or 101.5 video hours with fine-grained video text correspondence. Specifically, for each caption sentences, we find the start time and end time of the
video segment that matches the sentence.

#### Annotation files
The annotations and train/test/val split can be found in: `annotations/`

#### Annotation structure
The annotations for each caption sentence contains 4 fields:
 - id: a unique video id that can be used to located the video on YouTube
 - matched: 'Yes' if the sentence is grounded in the video, 'no' if the video is not located in the video.
 - begin_time: the start time of the video segment that corresponds to the sentence. If the sentence is not grounded in the video, the begin_time is zero.
 - end_time: the end time of the video segment  that corresponds to the sentence. If the sentence is not grounded in the video, the end_time is zero.


 
