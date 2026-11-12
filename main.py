#!/usr/bin/env python3
"""Coolest Art entry: writes the cosmic whale village art to /output/entry.png.

Deterministic: copies the same bytes every run.
"""
import os
import shutil
import sys

def main():
    # The art is stored alongside this script
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, 'art.png')
    out_dir = '/output'
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, 'entry.png')
    shutil.copyfile(src, dst)
    print(f'Wrote {dst} ({os.path.getsize(dst)} bytes)')

if __name__ == '__main__':
    main()
