import os

from fabric import Connection
import sys

user = 'ubuntu'


def copy_script(local_path, hosts):
    # Replace 'your_local_path' with the local path to your script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate the complete path
    complete_path = os.path.join(current_dir, local_path)

    # Replace 'your_remote_path' with the remote path on the server
    remote_path = '/home/{}/{}'.format(user, local_path.split('/')[-1])

    # Remote server
    for host in hosts:
        # Connect to the remote server
        with Connection(host=host, user=user) as c:
            # Upload the script to the remote server
            c.put(complete_path, remote_path)


if __name__ == "__main__":
    lpath = sys.argv[1]
    ips = sys.argv[2].split(',')
    ips = [ip.strip() for ip in ips]
    copy_script(lpath, ips)
