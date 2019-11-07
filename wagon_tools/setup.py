# -*- coding: UTF-8 -*-

""" Tools for setup.py in akd stack
"""

# Import from the Standard Library
from builtins import str
from glob import glob
from subprocess import Popen, PIPE
import sys

# Import from the setuptools_scm
from setuptools_scm import get_version


def get_git_hash():
    """
    Update in module a version.txt file with the git describe hash/tag info
    and the datetime commit info
    """
    # Get actual git describe
    command = ['git', 'describe', '--tags', '--long']
    popen = Popen(command, stdout=PIPE, stderr=PIPE, cwd='.')
    actual_git_version, stderrdata = popen.communicate()
    if popen.returncode != 0:
        raise EnvironmentError((popen.returncode, actual_git_version))
        # check that there is a tag if not request for one
    else:
        actual_git_version = str(actual_git_version, 'utf-8').strip()
    # 6-rc.1-0-ga23378a
    ver_patches, githash = actual_git_version.rsplit('-', 1)
    ver, patches = ver_patches.rsplit('-', 1)
    githash = githash[1:]
    return githash


def get_dt_version():
    """
    Update in module a version.txt file with the git describe hash/tag info
    and the datetime commit info
    Different cases:
      # no +
      1.4
      1.4.3
      # +
      1.3.dev0+nge2aadcb.d20161113
      1.4.4.dev0+ng8a6743d.d20161113
      1.4.4.dev1+nge54f78b
    """
    githash = get_git_hash()

    # Get date of actual git commit datetime
    command = ['git', 'show', githash, '--format="%ci"', '-s']
    popen = Popen(command, stdout=PIPE, stderr=PIPE, cwd='.')
    head_dt, stderrdata = popen.communicate()
    # python2/3 compatible
    head_dt = str(head_dt, 'utf-8')
    if popen.returncode != 0:
        raise EnvironmentError((popen.returncode, head_dt))
    else:
        head_dt = head_dt.rsplit('+', 1)[0].replace('"', '')
        head_dt = head_dt.strip()
        head_dt = head_dt.replace(' ', '_').rsplit(':', 1)[0]
        print("{}: Actual commit_version date".format(head_dt))
    # https://pypi.python.org/pypi/setuptools_scm_git_archive
    version = get_version()
    akd_version_long = '{}_{}'.format(version, head_dt)
    return akd_version_long


def write_version_with_dt(package):
    akd_version_long = get_dt_version()
    with open('{}/version.txt'.format(package), 'w') as version_file:
        version_file.write(akd_version_long)
    msg = '{}/version.txt fielled with : {}'
    print(msg.format(package, akd_version_long))


def print_egg_if_any():
    if 'bdist_egg' in sys.argv:
        egg_list = glob('dist/*.egg')
        # Use whith:
        # $ python setup.py bdist_egg --exclude-source-files or make egg
        if len(egg_list) == 1:
            egg = egg_list[0]
            msg = ("\n{header:#^69}\n"
                   "  egg ready at : {egg}\n"
                   "{stop:#^69}\n")
            print(msg.format(**dict(egg=egg, header=' bdist ', stop='')))
