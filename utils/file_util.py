import os
import shutil
from datetime import datetime
import utils.logging_util as logging
logger = logging.get_logger(__name__)

# create a tmp local work dir, return the dir path, optimisctically, there won't be more than one create action at same micro-second
def create_work_dir():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/work_dir/' + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")
    create_dir(path)
    logger.info('create work dir: %s' % path)
    return path

def create_dir(path):
    if os.path.exists(path):
        del_work_dir(path)
    os.makedirs(path)

def del_work_dir(path):
    logger.info('delete work dir: %s' % path)
    shutil.rmtree(path)

def work_dir(func):
    def wrapper(*args, **kwargs):
        path = create_work_dir()
        kwargs['work_dir'] = path
        r = func(*args, **kwargs)
        del_work_dir(path)
        return r
    return wrapper