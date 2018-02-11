#!/usr/bin/env python3

import click
import sys


CLICK_CONTEXT_SETTINGS = {'help_option_names': ('-h', '--help')}


@click.command(context_settings=CLICK_CONTEXT_SETTINGS)
def main():
    click.secho("Python {}".format(sys.version), bold=True, fg='green')


if __name__ == '__main__':
    main()
