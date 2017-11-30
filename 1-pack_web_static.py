#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the content
of the web_static folder of my AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime


def do_pack():
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(time)

    try:
        local("mkdir versions")
    except:
        pass
    if local("tar -cvzf {} web_static".format(archive)).succeeded:
        return archive
    else:
        return None
