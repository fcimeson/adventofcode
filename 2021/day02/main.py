#!/usr/bin/env python3

import re
import argparse

if __name__ == "__main__":

    # Args
    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("input", help="input file")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug code")
    args = parser.parse_args()

    # Part 1
    with open(args.input, "r") as f:
        horizontal = depth = 0
        for line in f.readlines():
            if re.match(r"^\s*forward\s*\d+\s*$", line):
                horizontal += int(re.findall(r"\d+", line)[0])
            elif re.match(r"^\s*down\s*\d+\s*$", line):
                depth += int(re.findall(r"\d+", line)[0])
            elif re.match(r"^\s*up\s*\d+\s*$", line):
                depth -= int(re.findall(r"\d+", line)[0])
            else:
                assert False
        print(f"Part 1: Horizontal = {horizontal}, Depth = {depth}, Product = {horizontal*depth}")

    # Part 2
    with open(args.input, "r") as f:
        horizontal = depth = aim = 0
        for line in f.readlines():
            if re.match(r"^\s*forward\s*\d+\s*$", line):
                value = int(re.findall(r"\d+", line)[0])
                horizontal += value
                depth += aim * value
            elif re.match(r"^\s*down\s*\d+\s*$", line):
                aim += int(re.findall(r"\d+", line)[0])
            elif re.match(r"^\s*up\s*\d+\s*$", line):
                aim -= int(re.findall(r"\d+", line)[0])
            else:
                assert False
        print(f"Part 2: Horizontal = {horizontal}, Depth = {depth}, Product = {horizontal*depth}")
