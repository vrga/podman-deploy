import re


def camel_case(input_string: str):
    reg = re.compile(r"([\w]*)(?:[\s\-_]*)")
    return re.sub(reg, lambda word: word.group(1).capitalize(), input_string)


class FilterModule(object):
    def filters(self):
        return {'camel_case': camel_case}
