#!/usr/bin/env python3

import os, shlex, subprocess
from natsort import natsorted


def find_audio_files(dir=os.getcwd(), exts=['.mp3', '.flac']):
    return natsorted([
        "'" + os.path.relpath(os.path.join(root, file), dir) + "'"
        for ext in exts for root, dirs, files in os.walk(dir) for file in files
        if file.lower().endswith(ext)
    ])


def find_cover(dir=os.getcwd(), exts=['.jpg']):
    l = [
        os.path.join(root, file) for ext in exts
        for root, dirs, files in os.walk(dir) for file in files
        if file.lower().endswith(ext)
    ]
    return "'" + os.path.relpath(
        sorted([(os.path.getsize(file), file) for file in l],
               key=lambda s: s[0])[-1][1], dir) + "'"


playlist = ' '.join(find_audio_files())
mpv = f'mpv --external-file={find_cover()} --force-window --image-display-duration=inf --vid=1 {playlist}'
subprocess.run(shlex.split(mpv))
