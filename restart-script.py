#!/usr/bin/env python


# Copyright (c) 2019 Konrad Pagacz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import logging
import time

import requests


WAIT_TIME = 60 * 1/20
URL = "https://apps.konsta.com.pl/app/glyculator/"
COMMANDS = """
systemctl restart shiny-server
"""


def check_url_response(url: str) -> bool:
    """Confirms the HTTP response from the provided url.
    Using HTTP requests attempts to check
    whether a site under the url is online.

    Args:
        url: url to a site

    Returns:
        True if site is online, False otherwise
    """
    with requests.get(url, timeout=5) as r:
        return r.ok


if __name__ == "__main__":
    # Logging config
    logging.basicConfig(filename="debug.log",
                        level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        filemode="w")

    while True:
        # Setting up a logger
        logger = logging.getLogger("")
        logger.setLevel(logging.ERROR)

        logger.info("Starting a check...")
        online = check_url_response(URL)
        if online:
            logger.info("Received HTTP response 200")
        else:
            logger.warning("Received error from HTTP request")
            logger.info("Attempting a restart...")
            os.system(COMMANDS)
            time.sleep(60 * 2)
            if check_url_response(URL):
                logger.info("Restart successful")
            else:
                logger.error("Restart unsuccessful")
                break

        logging.info("Sleeping...")
        time.sleep(WAIT_TIME)
