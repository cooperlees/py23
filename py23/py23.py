#!/usr/bin/env python3
""" Lets write some crappy py2 to convert to py3 """

# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)

import logging
import subprocess
import six
import sys

import click

from typing import Dict, Union  # noqa: F401


CLICK_CONTEXT_SETTINGS = {'help_option_names': ('-h', '--help')}
LOG = logging.getLogger(__name__)


def _handle_debug(
    ctx,    # type: click.core.Context
    param,  # type: Union[click.core.Option, click.core.Parameter]
    debug   # type: Union[bool, int, str]
):  # type: (...) -> Union[bool, int, str]
    '''Turn on debugging if asked otherwise INFO default'''
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        format=('[%(asctime)s] %(levelname)s: %(message)s ' +
                '(%(filename)s:%(lineno)d)'),
        level=log_level,
    )
    return debug


def binary_file_open(
    filename  # type: str
):  # type: (...) -> str
    with open(filename, 'rb') as ff:
        data = ff.read() if six.PY2 else ff.read().decode('utf-8')  # Py23

    return("I read in {} as {}".format(filename, type(data)))


def iteritems_fun(
    data,       # type: Dict[str, str]
    py_version  # type: int
):  # type: (...) -> str
    '''Iterate data and return the str with message'''

    # Py3: items defaults to an iterator in Py3
    # for version, message in data.items():
    # Py23: To be fully Py2 + 3 we can use the six iteritems wrapper - Py23
    # for version, message in six.iteritems(data):
    for version, message in data.iteritems():  # noqa: B301,T484 - Py2 Only
        if py_version == version:
            return "I am writing {}".format(message)

    LOG.error("We did not find {} in {}".format(py_version, data))
    return ''


def subprocess_echo(
    to_echo='"Hello World!"'  # type: str
):  # type: (...) -> str
    # if six.PY2:
    output = subprocess.check_output(['echo', to_echo])
    # else:
    #    output = subprocess.check_output(['echo', to_echo], encoding='utf-8')

    if output == (to_echo + '\n'):
        return (
            "echo of {} match. They are both {}".format(to_echo, type(output))
        )
    return (
        "echo of {} does not match. Returned output is {}".format(
            to_echo, type(output)
        )
    )


@click.command(context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(version='69')
@click.option(
    '-d', '--debug', is_flag=True, help='Turn on verbose logging',
    callback=_handle_debug, expose_value=False
)
@click.option(
    '--nofork', help='Do not risk forking!', is_flag=True
)
@click.pass_context
def main(
    ctx,    # type: click.core.Context
    nofork  # type: bool
):  # type: (...) -> None
    LOG.debug("Starting {} ...".format(sys.argv[0]))

    important_data = {
        2: 'lame Python 2 code',
        3: 'the future, aka, Python 3',
        4: 'some kind of crazy future shit',
    }

    # Lets print if we are lame or not
    print(iteritems_fun(important_data, int(sys.version[0])))

    # Is there differences with file opening?
    print(binary_file_open('/etc/hosts'))

    # Show click working and how awesome it is
    # Don't use argparse anymore - k thx ta
    if nofork:
        LOG.info("It's just too FORKING dangerous to fork")
    else:
        # Show subprocess fun
        print(subprocess_echo())

    ctx.exit(0)


if __name__ == '__main__':
    main()
