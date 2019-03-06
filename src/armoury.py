#usr/bin/python
import sys
from argparse import ArgumentParser

#from func import install, uninstall, init


def main(args):
    if args.operation == 'init':
        if args.type is None:
            print('init operation need the `type`.')
            sys.exit(1)

        if args.type == 'blocker':
            init.init_detector()
        
        if args.type == 'scanner':
            init.init_scanner()

        if args.type == 'signature':
            init.init_signature()


    if args.repository is None:
        print('install or uninstall operation need the `repository`.')
        sys.exit(1)

    if args.operation == 'install':
        install.install()

    if args.operation == 'remove':
        remove.remove()


if __name__ == '__main__':
    parser = ArgumentParser(
        description='package manager for buckler.',
        add_help=True
    )
    
    parser.add_argument(
        'operation',
        help='operation you want to do.',
        choices=['install', 'remove', 'init']    
    )
    parser.add_argument(
        '-r', '--repository',
        help='target repository url or auther/name for github.'
    )
    parser.add_argument(
        '-t', '--type',
        choices=['blocker', 'scanner', 'signature'],    
        help='type for project.'
    )

    args = parser.parse_args()
    print(args)
    main(args)
