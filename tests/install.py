import sys, os, pprint, subprocess
import unittest

sys.path.append('../src/')
from func import install


class TestPackage(unittest.TestCase):
    def setUp(self):
        os.system('mkdir .scanners')
        os.system('mkdir .signatures')

    def tearDown(self):
        os.system('rm -rf .scanners')
        os.system('rm -rf .signatures')

    def test_install_scanner(self):
        install.install_scanner('https://github.com/buckler-project/sample-scanner')
        files = subprocess.getoutput('ls .scanners')
        self.assertEqual('sample-scanner', files)
        print(f'path: {files}')

    def test_install_signature(self):
        install.install_signature('https://github.com/buckler-project/sample-signature')
        files = subprocess.getoutput('ls .signatures')
        self.assertEqual('sample-signature', files)
        print(f'path: {files}')

if __name__ == '__main__':
    unittest.main()
