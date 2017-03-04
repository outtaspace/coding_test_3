import argparse
import os
import sys

from city_info.command_factory import CommandFactory


def get_cli_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--all',
        action='store_true',
        help='provide summary information for all cities'
    )
    parser.add_argument(
        '--filename',
        type=str,
        help='optional filename holding the city info'
    )
    parser.add_argument(
        '--city',
        type=str,
        help='name of city'
    )

    return parser.parse_args()


def main():
    cli_options = get_cli_options()

    options = dict(writer=sys.stdout)

    if cli_options.all:
        options['mode'] = 'all'
    else:
        options['mode'] = 'city'
        options['city'] = cli_options.city

    if cli_options.filename is None:
        filename = os.path.abspath('./city_info.txt')
    else:
        filename = cli_options.filename
    options['reader'] = open(filename, 'r')

    command = CommandFactory.create(**options)
    command.execute()


main()
