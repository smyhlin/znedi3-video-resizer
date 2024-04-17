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
    parser.add_argument("-o", "--output", help="(optional default same as input folder) Output video path", type= str, required=False)
    parser.add_argument("-s", "--scale", help="(optional) Input resize scale: x2(default), x3, x4, x8", type= str, required=False)
    parser.add_argument("-p", "--presset", help="(optional) Input encode presset: h264, h265, nvenc, ffv1", type= str, required=False)
    parser.add_argument("-wr", "--widht", help="(optional) Video width resolution (default source*2)", type= int, required=False)
    parser.add_argument("-hr","--height", help="(optional) Video height resolution (default source*2)", type= int, required=False)
    return parser
 

def resize_video(video_path, video_settings, output_video):
    encode_vpy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           r"modules\encode.vpy")
    # https://forum.doom9.org/showthread.php?t=173094
    print(encode_vpy_path)
    command1 = f'VSPipe.exe --y4m --arg "video_path={video_path}" {encode_vpy_path} - | '
    command2 = f'ffmpeg -i pipe: -i "{video_path}" -map 0 -map 1:a -map 1:s? -c:v {video_settings} "{output_video}"'

    process1 = Popen(command1, stdout=PIPE, shell=False)
    process2 = Popen(command2, stdin=process1.stdout, stderr=PIPE)

    # while True:
    for i in range(10):
        line = process2.stderr.readline().decode('utf-8')
        print(line)

def get_video_settings_presset(args):
    video_settings = ''
    p=['user_friendly_numerator',
        'libx264 -crf 13 -preset slow -tune animation',
        'libx265 -crf 16 -preset slow -x265-params "sao=0:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3:ref=6"',
        'hevc_nvenc -preset p4 -profile:v main10 -b:v 5M',
        'ffv1'
        ]
    if not args.presset:
        while True:

            presset = (input(f'''Select one of the presset to encode resized video:
                            1: {p[1]} [VERY LOSSY, x264 good quality big size, OK compression, faster to encode]
                            2: {p[2]} [MEDIUM LOSSY, HEVC (x265) more efficient compression but slower to encode]
                            3: {p[3]} [LOSSY, HEVC compression with NVENC, fast encode using GPU but lower quality than CPU encoding]
                            4: {p[4]} [LOSELESS, FFV1 compression, fastest to encode but extremely large filesize (300+Gb per 20mib video)]\n\nPlease select one of the listed pressets: 1|2|3|4:'''))
            if presset in ['1','2','3','4']:
                video_settings = p[int(presset)]
                break
            else:
                print("Please select one of the listed pressets: 1|2|3|4")
    else:
        if args.presset == 'x264':
            video_settings = p[1]
        elif args.presset == 'x265':
            video_settings = p[2]
        elif args.presset == 'nvenc':
            video_settings = p[3]
        else:
            video_settings = 'ffv1'

    print(video_settings)

if __name__ == "__main__":
    parser = init_console_argument_parser()
    if len(sys.argv) < 2:
        print('Incorrect command.\nTry:\nresize.py -i video_path\nresize.py -i video_path -w 1280 -h 720\nresize.py -i video_path -p x4')
        print(parser.format_help())

    else:
        args=parser.parse_args()
        video_path = args.input
        output_video = args.output if args.output else os.path.dirname(video_path)
        video_settings = get_video_settings_presset(args)

        if args.height:
            pass
        if args.widht:
            pass

        resize_video(video_path, video_settings, output_video)
        # clip = core.lsmas.LWLibavSource(video_path)
        # mode=
        #       znedi3, faster CPU implementation
        #       nnedi3, original CPU implementation
        #       nnedi3cl, OpenCL implementation, with a new option device to specify the desired device (refer to )
        # clip = nnedi3_resample(clip, clip.width * 2, clip.height * 2, mode='znedi3')
        # clip.set_output()