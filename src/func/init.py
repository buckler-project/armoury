import os, urllib.request

def init_project(url, file_name):
    urllib.request.urlretrieve(
        url,
        f"{file_name}"
    )

def init_detector():
    init_project("https://github.com/buckler-project/config-templates/raw/master/buckler.yml", "buckler.yml")
    os.mkdir(".scanners")
    os.mkdir(".signatures")

def init_scanner():
    init_project("https://github.com/buckler-project/config-templates/raw/master/scanner.yml", "scanner.yml")

def init_signature():
    init_project("https://github.com/buckler-project/config-templates/raw/master/signature.yml", "signature.yml")
