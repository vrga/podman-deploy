def camel_case(string: str):
    def _hanle_separator(input_str: str, sep: str):
        return ''.join(word.title() for word in input_str.split(sep))

    for _sep in ('-', '_', ' '):
        string = _hanle_separator(string, _sep)

    return string


class FilterModule(object):
    def filters(self):
        return {'camel_case': camel_case}
