
def save_site_to_file(name, site):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(site)


def read_site_from_file(name):
    with open(name, encoding='utf-8') as file:
        src = file.read()

    return src