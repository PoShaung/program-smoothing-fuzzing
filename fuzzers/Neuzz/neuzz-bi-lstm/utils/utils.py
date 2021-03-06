import os
import time
import shutil
import shlex
import subprocess
import logging


def init_logger(file_name, verbose=1, name=None):
    level_dict = {0: logging.DEBUG, 1: logging.INFO, 2: logging.WARNING}
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s][%(levelname)s] %(message)s"
    )
    logger = logging.getLogger(name)
    logger.setLevel(level_dict[verbose])

    fh = logging.FileHandler(file_name, 'w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def obtain_max_seed_size(seed_path):
    out = os.popen(f'ls -S {seed_path} | head -1')
    file_path = os.path.join(seed_path, out.read().split()[0])
    return os.path.getsize(file_path)


def move_file(src_path, dst_path):
    if not os.path.isfile(src_path):
        return
    fpath, fname = os.path.split(dst_path)
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    shutil.move(src_path, dst_path)


def acquire_edge(showmap_path, seed_path, program_execute):
    showmap_cmd = f'{showmap_path} -q -o /dev/stdout -m 512 -t 500 ./{program_execute} {seed_path}'
    try:
        output = subprocess.check_output(shlex.split(showmap_cmd))
    except subprocess.CalledProcessError:
        return list()
    edge_list = [int(line.split(b':')[0]) for line in output.splitlines()]
    return edge_list
