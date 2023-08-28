'''
References:
https://www.cloudskillsboost.google/focuses/1074?parent=catalog
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/developingapps/python/devenv/list-gce-instances.py
https://www.c-sharpcorner.com/article/creating-python-application-development-environment-in-google-cloud-platform/

'''

# pip install google-api-python-client

# WHERE TO EXECUTE THIS?

import argparse
import os
import time

import googleapiclient.discovery

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']


def main(project, zone):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(' - ' + instance['name'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument(
        '--zone',
        default='us-central1-f',
        help='Compute Engine zone to deploy to.')

    args = parser.parse_args()

    main(args.project_id, args.zone)

