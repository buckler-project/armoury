import sys, os, pprint, subprocess
import unittest

sys.path.append('../src/')

from package.signature import Signature, SignatureFactory


class TestPackage(unittest.TestCase):
    def setUp(self):
        os.system('mkdir .signatures')
        os.system('mkdir .signatures/buckler-project')
        os.system('cd .signatures/buckler-project && git clone https://github.com/buckler-project/sample-signature')

    def tearDown(self):
        os.system('rm -rf .signatures')

    def test_generate_signature(self):
        factory = SignatureFactory()
        signature = factory.generate(auther='buckler-project', name='sample-signature')

        self.assertEqual('buckler-project', signature.auther)
        self.assertEqual('sample-signature', signature.name)
        self.assertEqual('https://github.com/buckler-project/sample-signature', signature.url)

        self.assertEqual('.signatures/buckler-project/sample-signature', signature.get_path())
        self.assertEqual('.signatures/buckler-project/sample-signature/signature.yml', signature.get_config_path())

    def test_generate_signature_from_url(self):
        factory = SignatureFactory()
        signature = factory.generate_from_url('https://github.com/buckler-project/sample-signature')

        self.assertEqual('buckler-project', signature.auther)
        self.assertEqual('sample-signature', signature.name)
        self.assertEqual('https://github.com/buckler-project/sample-signature', signature.url)

        self.assertEqual('.signatures/buckler-project/sample-signature', signature.get_path())
        self.assertEqual('.signatures/buckler-project/sample-signature/signature.yml', signature.get_config_path())


if __name__ == '__main__':
    unittest.main()
