#!/usr/bin/python3
"""
2-do_deploy_web_static.py

Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""
from os.path import exists
from fabric.api import env, put, run

env.hosts = ['54.160.70.107', '54.237.63.194']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    # Check of archive is exists
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = "/data/web_static/releases/" + archive_name[:-4]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        run(f"sudo mkdir -p {archive_folder}")
        run(f"sudo tar -xzf /tmp/{archive_name} -C {archive_folder}")

        # Delete the archive from the web server
        run(f"sudo rm /tmp/{archive_name}")

        # Delete the symbolic link /data/web_static/current from the web server
        run(f"sudo mv {archive_folder}/web_static/* {archive_folder}")
        run(f"sudo rm -rf {archive_folder}/web_static")
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on web server
        run(f"sudo ln -s {archive_folder} /data/web_static/current")

        return True

    except Exception:
        return False
