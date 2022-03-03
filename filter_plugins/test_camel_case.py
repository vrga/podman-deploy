from .camel_case import camel_case

assert camel_case('test-string') == 'TestString'
assert camel_case('test string') == 'TestString'
assert camel_case('test string asdfger1') == 'TestStringAsdfger1'
assert camel_case('test string 21') == 'TestString21'
assert camel_case('test string 1asdfq') == 'TestString1asdfq'
assert camel_case('pod-container-docker-registry.service') == 'PodContainerDockerRegistryService'
