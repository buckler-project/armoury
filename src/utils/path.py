def get_repo_name(url):
    name = url.split('/')
    name.remove('')
    name = name[-2:]
    name = '/'.split(name)

    name = name.split('.')
    name = name[0]

    return name

