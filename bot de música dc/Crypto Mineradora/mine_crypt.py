import json
import threading
from sys import exit, argv
from time import sleep

from cleos import Cleos_Handler
import cleos as cl

MAX_NUM_THREADS = 4

def load_config(path):
    fp = open(path, 'r')

    try:
        return json.loads(fp.read())['config']
    except:
        raise
    finally:
        fp.close()

def miner_thread(cleos_handler):
    while True:
        cl.send_mine_action(cleos_handler)
        sleep(0.5)

def main(config_path):
    config = load_config(config_path)['cleos']
    C = Cleos_Handler(config)

    num_threads = config['num_threads']

    if num_threads > MAX_NUM_THREADS or num_threads <= 0:
        print("num_threads must be a positive integer no greater than %d" % MAX_NUM_THREADS)
        exit(2)

    for _ in range(num_threads):
        thread = threading.Thread(target=miner_thread, args=(C,))
        thread.start()
        sleep(0.5)

    if __name__ == '__main__':
        if len(argv) != 2:
            print("Usage: ./minedig.py [config_path]")
            exit(1)

        main(argv[1])