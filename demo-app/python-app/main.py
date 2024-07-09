#!/usr/bin/env python

import logging
import os
import time

logging.basicConfig(format='%(asctime)s %(name)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', logging.INFO))

INTERVAL = 1200


def main():
    print(f"The current time is {time.asctime()}")


if __name__ == '__main__':
    try:
        while True:
            main()
            time.sleep(INTERVAL)

    except Exception as e:
        logger.error(e, exc_info=True)
