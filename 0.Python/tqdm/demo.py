from tqdm import tqdm
import time

def do_something():
    """Do something here"""
    time.sleep(0.1)

if __name__ == '__main__':
    for i in tqdm(range(100), total=100, ncols=100, unit='item'):
            do_something()