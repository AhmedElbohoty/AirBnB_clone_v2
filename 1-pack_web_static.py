#!/usr/bin/python3
"""
1-pack_web_static.py

Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from os import path
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        local("sudo mkdir -p versions")

        # Get date
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")

        # Get file name
        file_name = f"web_static_{time_format}.tgz"

        # Get file path
        path = f"versions/{file_name}"

        # Compress
        local(f"tar -czvf {path} web_static")

        return path
    except Exception:
        return None
