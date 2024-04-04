#!/usr/bin/python3
"""
1-pack_web_static.py
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        local("sudo mkdir -p versions")

        # Generate file name
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(time_format)

        # Compress
        local(f"tar -czvf versions/{file_name} web_static")

        return f"versions/{file_name}"
    except Exception:
        return None
