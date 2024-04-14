# -*- coding: utf-8 -*-
import argparse, sys
import vapoursynth as vs
from vapoursynth import core
from modules.nnedi3_resample import nnedi3_resample


def init_console_argument_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="Input video path", type= str, required=True)
    parser.add_argument("-wr", "--widht", help="Video width resolution (default source*2)", type= int, required=False)
    parser.add_argument("-hr","--height", help="Video height resolution (default source*2)", type= int, required=False)
    return parser


def resize_video(input_path):
    # Load the original video using ffms2 plugin
    clip = core.ffms2.Source(input_path)
    
    # Resize the video using nnedi3_resample
    clip = nnedi3_resample(clip, clip.width * 2, clip.height * 2, mode='znedi3')
    
    # Write the processed frames to a video file
    clip.set_output()

if __name__ == "__main__":
    parser = init_console_argument_parser()
    if len(sys.argv) < 2:
        print('Incorrect command.\nTry:\nresize.py -i video_path\nresize.py -i video_path -w 1280 -h 720\n')
        print(parser.format_help())

    else:
        args=parser.parse_args()
        video_path = args.input
        if args.height:
            pass
        if args.widht:
            pass
        
        resize_video(video_path)
        # clip = core.lsmas.LWLibavSource(video_path)
        # mode=
        #       znedi3, faster CPU implementation
        #       nnedi3, original CPU implementation
        #       nnedi3cl, OpenCL implementation, with a new option device to specify the desired device (refer to )
        # clip = nnedi3_resample(clip, clip.width * 2, clip.height * 2, mode='znedi3')
        # clip.set_output()