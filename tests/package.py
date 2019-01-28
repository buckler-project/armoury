import sys, os, pprint, subprocess
import unittest

sys.path.append(os.pardir)

from src.packages.package import Package


class TestPackage(unittest.TestCase):
    def setUp(self):
        os.system("mkdir data")
        self.pkg = Package()
        self.pkg.path = "data"

    def tearDown(self):
        os.system("rm -r data")

    def test_package(self):
        self.pkg.install("https://github.com/buckler-project/sample-scanner")
        files = subprocess.getoutput("ls data/")
        self.assertEqual('sample-scanner', files)
        print(f"path: {files}")

        self.pkg.uninstall("sample-scanner")
        files = subprocess.getoutput("ls data/")
        self.assertEqual('', files)
        print(f"path: {files}")


if __name__ == "__main__":
    unittest.main()
