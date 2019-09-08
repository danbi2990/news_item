import os


def get_files(dir_):
    return [f for f in os.listdir(dir_) if '.csv' in f]


def validate_file(file):
    with open(file) as f:
        text = f.read()
    return not (('fail' in text) and ('error' in text))


def get_valid_files(dir_):
    return [f for f in get_files(dir_) if validate_file(dir_ + f)]


def get_downloaded_regions(dir_):
    return [file.split('-')[1] for file in get_valid_files(dir_) if '.csv' in file]
