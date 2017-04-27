import requests
import json
from datetime import timedelta, datetime
import time

status_api = 'http://10.10.129.141:11000/oozie/v1/job/%s'
trigger_api = 'http://10.10.129.141:11000/oozie/v1/jobs?action=start'

class Job:
    def __init__(self, job_id, job_status, job_config, retry=2):  # job_id is the workflow id
        self.job_id = job_id
        self.job_status = job_status
        self.job_config = job_config
        self.retry = retry


def _build_job(template, args):
    job_config = template % args
    return Job(None, None, job_config)


def _get_job_status(job_id):
    resp = requests.get(status_api % job_id)
    return json.loads(resp.text)['status']

def _trigger_job(job):
    resp = requests.post(
        url=trigger_api,
        data=job.job_config,
        headers={'Content-Type': 'application/xml;charset=UTF-8'}
    )
    if resp.status_code == 201:
        job_id = json.loads(resp.text)['id']
        job.job_id = job_id
    else:
        job.status = 'ERROR'
    return job


def _date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n + 1)


def _execute_jobs_parallel(jobs, concurrency, sleep_interval):
    first_batch_jobs = jobs[:concurrency]
    for job in first_batch_jobs:
        _trigger_job(job)

    while True:
        time.sleep(sleep_interval)
        # refresh job status and remove the SUCCEEDED one
        running_count = 0
        for job in jobs:
            if job.job_id is not None:
                job_status = _get_job_status(job.job_id)
                if job_status == 'SUCCEEDED':
                    jobs.remove(job)
                    #logger.info('job: %s, %s is completed' % (str(job.area), str(job.partition_id)))
                elif job_status == 'RUNNING':
                    running_count += 1
                else:            # other status, such as 'KILLED', 'ERROR'
                    if job.retry > 0:
                        job.job_id = None
                        job.job_status = None
                        job.retry -= 1
                    else:
                        jobs.remove(job)

        # trigger new jobs
        ready_to_trigger = concurrency - running_count
        for job in jobs:
            if ready_to_trigger <= 0:
                break
            if job.job_id is None and ready_to_trigger > 0:
                _trigger_job(job)
                ready_to_trigger -= 1
        # stop the loop when all jobs are done.
        if len(jobs) == 0:
            break


def _execute_jobs_sequence(jobs, sleep_interval):
    job = jobs.pop(0)
    _trigger_job(job)
    print('yyy')
    while True:
        time.sleep(sleep_interval)
        if job.job_id is not None:
            job_status = _get_job_status(job.job_id)
            if job_status == 'SUCCEEDED':
                if len(jobs) == 0:
                    break
                else:
                    job = jobs.pop(0)
                    _trigger_job(job)
                    print('yyy')
            elif job_status == 'RUNNING':
                continue
            else:  # other status, such as 'KILLED', 'ERROR'
                if job.retry > 0:
                    job.job_id = None
                    job.job_status = None
                    job.retry -= 1
                else:
                    jobs.remove(job)

