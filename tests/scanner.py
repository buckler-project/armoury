import sys, os, pprint, subprocess
import unittest

sys.path.append('../src/')

from package.scanner import Scanner, ScannerFactory


class TestPackage(unittest.TestCase):
    def setUp(self):
        os.system('mkdir .scanners')
        os.system('mkdir .scanners/buckler-project')
        os.system('cd .scanners/buckler-project && git clone https://github.com/buckler-project/sample-scanner')

    def tearDown(self):
        os.system('rm -rf .scanners')

    def test_generate_scanner(self):
        factory = ScannerFactory()
        scanner = factory.generate(auther='buckler-project', name='sample-scanner')

        self.assertEqual('buckler-project', scanner.auther)
        self.assertEqual('sample-scanner', scanner.name)
        self.assertEqual('https://github.com/buckler-project/sample-scanner', scanner.url)

        self.assertEqual('.scanners/buckler-project/sample-scanner', scanner.get_path())
        self.assertEqual('.scanners/buckler-project/sample-scanner/scanner.yml', scanner.get_config_path())

    def test_generate_scanner_from_url(self):
        factory = ScannerFactory()
        scanner = factory.generate_from_url('https://github.com/buckler-project/sample-scanner')

        self.assertEqual('buckler-project', scanner.auther)
        self.assertEqual('sample-scanner', scanner.name)
        self.assertEqual('https://github.com/buckler-project/sample-scanner', scanner.url)

        self.assertEqual('.scanners/buckler-project/sample-scanner', scanner.get_path())
        self.assertEqual('.scanners/buckler-project/sample-scanner/scanner.yml', scanner.get_config_path())


if __name__ == '__main__':
    unittest.main()
