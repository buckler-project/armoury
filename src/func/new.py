import os, urllib.request

def build_new_project(url, project_name, file_name):
    os.mkdir(project_name)

    urllib.request.urlretrieve(
        url,
        f"{project_name}/{file_name}"
    )

    os.system(f"cd {project_name} && git init")


def new_detector(name):
    build_new_project("https://github.com/buckler-project/config-templates/raw/master/buckler.yml", name, "buckler.yml")
    os.mkdir(f"{name}/.scanners")
    os.mkdir(f"{name}/.signatures")

def new_scanner(name):
    build_new_project("https://github.com/buckler-project/config-templates/raw/master/scanner.yml", name, "scanner.yml")

def new_signature(name):
    build_new_project("https://github.com/buckler-project/config-templates/raw/master/signature.yml", name, "signature.yml")
