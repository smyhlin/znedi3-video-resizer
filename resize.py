# -*- coding: utf-8 -*-
import subprocess
import os
from subprocess import Popen, PIPE, STDOUT
import argparse, sys
import vapoursynth as vs
from vapoursynth import core
from modules.nnedi3_resample import nnedi3_resample


def init_console_argument_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input video path (default x2 presset enabled)", type= str, required=True)
    parser.add_argument("-p", "--presset", help="(optional) Input resize preset: x2(default), x3, x4, x8", type= str, required=False)
    parser.add_argument("-wr", "--widht", help="(optional) Video width resolution (default source*2)", type= int, required=False)
    parser.add_argument("-hr","--height", help="(optional) Video height resolution (default source*2)", type= int, required=False)
    return parser


def resize_video(video_path, video_settings, output_video):
    command1 = f'VSPipe.exe --y4m --arg "video_path={video_path}" C:/Users/myself/Desktop/script.vpy -'
    command2 = f'ffmpeg -i pipe: -i "{video_path}" -map 0 -map 1:a -map 1:s? -c:v {video_settings} "{output_video}"'

    process1 = Popen(command1, stdout=PIPE, shell=False)
    process2 = Popen(command2, stdin=process1.stdout, stderr=PIPE)

    while True:
        line = process2.stderr.readline().decode('utf-8')
        print(line)

if __name__ == "__main__":
    parser = init_console_argument_parser()
    if len(sys.argv) < 2:
        print('Incorrect command.\nTry:\nresize.py -i video_path\nresize.py -i video_path -w 1280 -h 720\nresize.py -i video_path -p x4')
        print(parser.format_help())

    else:
        args=parser.parse_args()
        video_path = args.input
        if args.presset:
            pass
        if args.height:
            pass
        if args.widht:
            pass

        video_settings='libx264 -crf 13 -preset slow -tune animation'
        output_video = 'same_as_input'
        resize_video(video_path, video_settings, output_video)
        # clip = core.lsmas.LWLibavSource(video_path)
        # mode=
        #       znedi3, faster CPU implementation
        #       nnedi3, original CPU implementation
        #       nnedi3cl, OpenCL implementation, with a new option device to specify the desired device (refer to )
        # clip = nnedi3_resample(clip, clip.width * 2, clip.height * 2, mode='znedi3')
        # clip.set_output()