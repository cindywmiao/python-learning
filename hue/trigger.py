from datetime import timedelta, datetime
import utils.driver_util as driver_util
from utils.arg_util import forecast_input_gathering_driver_parser


def _config_template():
    return """
           <configuration>
              <property>
                <name>oozie.wf.application.path</name>
                <value>hdfs://nameservice1/user/mercury/oozie/workspaces/%s</value>
              </property>
              <property>
                <name>user.name</name>
                <value>mercury</value>
              </property>
              <property>
                <name>oozie.use.system.libpath</name>
                <value>True</value>
              </property>
              <property>
                <name>mapreduce.job.user.name</name>
                <value>mercury</value>
              </property>
              <property>
                <name>security_enabled</name>
                <value>False</value>
              </property>
              <property>
                <name>nameNode</name>
                <value>hdfs://nameservice1</value>
              </property>
              <property>
                <name>dryrun</name>
                <value>False</value>
              </property>
              <property>
                <name>jobTracker</name>
                <value>yarnRM</value>
              </property>
            </configuration>
           """


def main():

    workflow_id = "hue-oozie-1485224167.62"

    args_template = (workflow_id)

    # create a job with config_template
    job = driver_util._build_job(_config_template(), args_template)

    # execute the job
    driver_util._trigger_job(job)




if __name__ == '__main__':main()