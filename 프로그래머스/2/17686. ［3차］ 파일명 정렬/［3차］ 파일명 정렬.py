import re

def solution(files):
    def parse_file(file):
        match = re.match(r"([^\d]+)(\d+)(.*)", file)
        return match.groups()
    sorted_files = sorted(files, key=lambda file: (parse_file(file)[0].lower(), int(parse_file(file)[1])))
    return sorted_files