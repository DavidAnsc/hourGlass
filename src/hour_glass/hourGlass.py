#!/usr/bin/env python3
"""
Fancy ASCII hourglass generator

Usage:
  python3 fancy_hourglass.py -H 32 -W 72

Rules:
- height and width must be positive even integers
- width must be >= height
- height is the number of rows of the hourglass body (not counting top/bottom dashed borders)
"""

import argparse
import sys

def parse_even(name, s):
    try:
        v = int(s)
    except Exception:
        raise argparse.ArgumentTypeError(f"{name} must be an integer")
    if v <= 0 or (v % 2) != 0:
        raise argparse.ArgumentTypeError(f"{name} must be a positive even integer")
    return v

def dashed_line(width, dash='- '):
    # produce a dashed-looking line ~width chars long (dash string repeated and trimmed)
    rep = (dash * ((width // len(dash)) + 2))[:width]
    return rep

def generate_fancy_hourglass(height: int, width: int, dash_lines: int = 3) -> str:
    if height % 2 != 0 or width % 2 != 0:
        raise ValueError("height and width must be even integers")
    if width < height:
        raise ValueError("width must be >= height")

    half = height // 2
    lines = []

    # top dashed border (a few lines)
    for _ in range(dash_lines):
        lines.append(dashed_line(width))

    # top half (sloping inward)
    for r in range(half):
        # left and right positions (make slope fairly steep by using step 2)
        left = r * 2
        right = width - 1 - r * 2

        # start with spaces
        row = [' '] * width

        gap = right - left

        # if we reached the narrow waist region (or overlap), render a small waist block
        if gap <= 3:
            # form a tiny waist: two central pillars '||' or ']['
            mid_left = left
            mid_right = right
            # keep them visible even if they coincide
            row[mid_left] = '|'
            row[mid_right] = '|'
            # small decorative inner stitches above/below waist
            if mid_right - mid_left > 1:
                row[mid_left + 1] = ' '
        else:
            # decorate left diagonal with alternating pattern to create the stitched effect
            # pattern cycles so diagonals look like: \ | \ | \  and mirrored / | / | / 
            # choose which to put at main diagonal position and at the "inner" neighbor
            if r % 2 == 0:
                row[left] = '\\'      # backslash at outer edge
                row[left + 1] = '|'   # vertical "stitch" just inside it
            else:
                row[left] = '|'       # vertical at outer edge (dotted look)
                # put a small diagonal just inside
                if left + 1 < width:
                    row[left + 1] = '\\'

            # right side mirrored
            if r % 2 == 0:
                row[right] = '/'      # forward slash at outer edge
                row[right - 1] = '|'  # vertical "stitch" just inside
            else:
                row[right] = '|'      # vertical at outer edge
                if right - 1 >= 0:
                    row[right - 1] = '/'

            # add a soft inner connector every few lines to emphasize narrowing
            if r % 3 == 0 and gap > 6:
                # put a small '>' leaning inward on left, '<' on right
                if left + 2 < right - 2:
                    row[left + 2] = '>'
                    row[right - 2] = '<'

        lines.append(''.join(row))

    # waist: a couple of lines where hourglass is narrowest (mirror of joint)
    # produce two waist rows with small pillars and inner vertical stitches
    waist_rows = 2
    waist_left = (half - 1) * 2
    waist_right = width - 1 - (half - 1) * 2
    for wrow in range(waist_rows):
        row = [' '] * width
        # central pillars (two columns) always present
        row[waist_left] = '|'
        row[waist_right] = '|'
        # decorate between them occasionally
        if waist_right - waist_left > 1 and wrow % 2 == 0:
            row[waist_left + 1: waist_right] = [' '] * (waist_right - waist_left - 1)
        lines.append(''.join(row))

    # bottom half (mirror of top half but inverted patterns)
    for r in reversed(range(half)):
        left = r * 2
        right = width - 1 - r * 2
        row = [' '] * width
        gap = right - left
        if gap <= 3:
            row[left] = '|'
            row[right] = '|'
        else:
            # inverted decorations: use '/' on left, '\' on right to mirror
            if r % 2 == 0:
                row[left] = '/'        # left uses forward slash on bottom half
                row[left + 1] = '|'    # stitch
            else:
                row[left] = '|'        # vertical
                if left + 1 < width:
                    row[left + 1] = '/'

            if r % 2 == 0:
                row[right] = '\\'      # backslash on right
                row[right - 1] = '|'   # stitch
            else:
                row[right] = '|'
                if right - 1 >= 0:
                    row[right - 1] = '\\'

            if r % 3 == 0 and gap > 6:
                if left + 2 < right - 2:
                    row[left + 2] = '<'
                    row[right - 2] = '>'

        lines.append(''.join(row))

    # bottom dashed border
    for _ in range(dash_lines):
        lines.append(dashed_line(width))

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fancy ASCII hourglass generator")
    parser.add_argument('-H', '--height', type=lambda s: parse_even('height', s), help="hourglass height (even integer)", required=False)
    parser.add_argument('-W', '--width', type=lambda s: parse_even('width', s), help="total width (even integer)", required=False)
    args = parser.parse_args()

    if args.height is None or args.width is None:
        try:
            h = int(input("Enter even height (body rows, e.g. 32): ").strip())
            w = int(input("Enter even width (columns, e.g. 72): ").strip())
            if h <= 0 or w <= 0 or (h % 2 != 0) or (w % 2 != 0):
                print("Height and width must be positive even integers. Exiting.")
                sys.exit(1)
            args.height, args.width = h, w
        except (ValueError, KeyboardInterrupt):
            print("\nInvalid input or cancelled. Exiting.")
            sys.exit(1)

    try:
        art = generate_fancy_hourglass(args.height, args.width)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    print(art)


if __name__ == "__main__":
    main()
