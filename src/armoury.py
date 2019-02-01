#usr/bin/python
import sys
from func import install, uninstall, new


def main(argv):
    if argv[1] == 'install':
        if argv[2] == 'scanner':
            install.install_scanner(argv[3])
            sys.exit(0)

        elif argv[2] == 'signature':
            install.install_signature(argv[3])
            sys.exit(0)

    if argv[1] == 'uninstall':
        if argv[2] == 'scanner':
            uninstall.uninstall_scanner(argv[3])
            sys.exit(0)

        elif argv[2] == 'signature':
            uninstall.uninstall_signature(argv[3])
            sys.exit(0)
    
    if argv[1] == 'new':
        if argv[2] == 'detector':
            new.new_detector(argv[3])
            sys.exit(0)
        
        elif argv[2] == 'scanner':
            new.new_scanner(argv[3])
            sys.exit(0)

        elif argv[2] == 'signature':
            new.new_signature(argv[3])
            sys.exit(0)


    else:
        print('argument not correct')
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("not enough argument")
    else:
        main(sys.argv)
