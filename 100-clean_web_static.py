#!/usr/bin/python3
"""This module contains methods"""
from fabric.api import local, run, env
env.hosts = ["3.95.32.69", "54.144.129.181"]


def do_clean(number=0):
    """Method that deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'
          .format(number))
    path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'
        .format(path, number))
