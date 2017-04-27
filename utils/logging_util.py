import logging
import sys

root = logging.getLogger()
root.setLevel(logging.WARNING)

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


# disable requests module info message.
logging.getLogger("requests").setLevel(logging.WARNING)


def get_logger(py_module):
    return logging.getLogger(py_module)
