from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    prepend_slash = path.startswith('/')
    dirs = path.split('/')
    output = []

    for dir in dirs:
        if dir == '.' or dir == '':
            continue
        elif dir == '..' and len(output) and output[-1] != '..':
            output.pop()
        else:
            output.append(dir)

    if prepend_slash and len(output):
        output[0] = f'/{output[0]}'

    if not len(output):
        output.append('/')

    return '/'.join(output)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
