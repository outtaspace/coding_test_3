import argparse
import os
import sys


def get_cli_options():
    parser = argparse.ArgumentParser()

    parser.add_argument('--all', action='store_true', help='provide summary information for all cities')
    parser.add_argument('--filename', type=str, help='optional filename holding the city info')
    parser.add_argument('--city', type=str, help='name of city')

    return parser.parse_args()


def main():
    options = get_cli_options()
    print(options)

    filename = options.filename
    if filename is None:
        filename = os.path.abspath(__file__)

    xargs = dict(
        reader=open(filename, 'r'),
        writer=sys.stdout,
        city=options.city
    )

    command = command_factory.create('city' if options.city else 'all', xargs)
    command.execute()

if __name__ == '__main__':
    main()
