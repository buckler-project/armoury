#usr/bin/python
import sys
from func import install, uninstall, init


def main(argv):
    if argv[1] == 'install':
        if len(argv) < 4:
            print("not enough argument")
            sys.exit(1)

        if argv[2] == 'scanner':
            install.install_scanner(argv[3])
            sys.exit(0)

        elif argv[2] == 'signature':
            install.install_signature(argv[3])
            sys.exit(0)

    if argv[1] == 'uninstall':
        if len(argv) < 4:
            print("not enough argument")
            sys.exit(1)

        if argv[2] == 'scanner':
            uninstall.uninstall_scanner(argv[3])
            sys.exit(0)

        elif argv[2] == 'signature':
            uninstall.uninstall_signature(argv[3])
            sys.exit(0)
    
    if argv[1] == 'init':
        if len(argv) < 3:
            print("not enough argument")
            sys.exit(1)

        if argv[2] == 'blocker':
            init.init_detector()
            sys.exit(0)
        
        elif argv[2] == 'scanner':
            init.init_scanner()
            sys.exit(0)

        elif argv[2] == 'signature':
            init.init_signature()
            sys.exit(0)

    else:
        print('argument not correct')
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
