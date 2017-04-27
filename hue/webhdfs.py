import utils.hdfs_util as hdfs_util

workspace = '../work_dir/'

hdfs_path = '/user/mercury/oozie/workspaces/hue-oozie-1485224167.62/workflow.xml'


hdfs_util.upload_file(workspace + 'workflow.xml', hdfs_path)