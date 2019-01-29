import sys, os, pprint, subprocess
import unittest

sys.path.append('../src/')
from func import install
from func import uninstall


class TestPackage(unittest.TestCase):
    def setUp(self):
        os.system('mkdir .scanners')
        os.system('mkdir .signatures')

        install.install_scanner('https://github.com/buckler-project/sample-scanner')
        install.install_signature('https://github.com/buckler-project/sample-signature')

    def tearDown(self):
        os.system('rm -rf .scanners')
        os.system('rm -rf .signatures')

    def test_install_scanner(self):
        uninstall.uninstall_scanner('buckler-project/sample-scanner')
        files = subprocess.getoutput('ls .scanners')
        self.assertEqual('', files)

    def test_install_signature(self):
        uninstall.uninstall_signature('buckler-project/sample-signature')
        files = subprocess.getoutput('ls .signatures')
        self.assertEqual('', files)


if __name__ == '__main__':
    unittest.main()
