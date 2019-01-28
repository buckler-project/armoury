def get_repo_name(url):
    name = url.split('/')
    name.remove('')
    name = name[-1]

    name = name.split('.')
    name = name[0]

    return name
