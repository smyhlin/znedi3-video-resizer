# znedi3-video-resizer

A powerful and versatile video resizing tool based on nnedi3 -> znedi3 utils focused on easy of use and user-friendly usage.
This program allows you to easily resize your video files to your desired dimensions or select from predefined presets.

#### Features:

Resizes videos to custom width, height, or both.
Offers common video resolution presets (e.g., 720p, 1080p) for quick selection.
Supports various video formats (compatibility may depend on your system's libraries).

#### Installation:
```pip install -r requirements.txt``` 
>Also ffmpeg needed t obe added to PATH env:
>https://www.wikihow.com/Install-FFmpeg-on-Windows
___
#### Usage:
Just for now just run `rezise_encode.bat` and change params inside it to your wish:
select input \ output path and encoder.


# Temporaly not worked:
## TODO:
* make more detailed instruction
* finish interactive run
* add GUI
```CMD

```znedi3-video-resizer <input_video> <output_video> [options]```
___
#### Options:
> -i, --input <width>: Specify the desired output video width (pixels).

> -wr, --width <width>: Specify the desired output video width (pixels).

> -hr, --height <height>: Specify the desired output video height (pixels).

> -p, --preset <preset>: Select a predefined video resolution preset (e.g., 720p, 1080p).
___
#### Examples:

Resize a video to a custom width and height:
CMD

```znedi3-video-resizer input.mp4 output.avi -w 640 -h 480```

Resize a video using a preset resolution:
CMD

```znedi3-video-resizer my_video.mkv resized_video.mp4 -p 1080p```
```
___
#### Additional Notes:

For a complete list of supported video formats and available options, refer to the [ffmpeg's documentation](https://ffmpeg.org/ffmpeg-formats.html)

## 💝Credits💝:
* ❤All donors❤
* VapourSynth: https://vapoursynth.com/
* mvsfunc: https://github.com/HomeOfVapourSynthEvolution/mvsfunc
* nnedi3_resample: https://github.com/HomeOfVapourSynthEvolution/nnedi3_resample
* znedi3: https://github.com/sekrit-twc/znedi3
* fmtconv: https://gitlab.com/EleonoreMizo/fmtconv/
* ffms2: https://github.com/FFMS/ffms2
* FFmpeg: https://ffmpeg.org/
* FFmpeg Builds - gyan.dev: https://www.gyan.dev/ffmpeg/builds/
* Python: https://www.python.org/

We welcome contributions to this project! If you'd like to help improve znedi3-video-resizer.

## License:
GPLv3
