import os

import testinfra.utils.ansible_runner
from testinfra.host import Host

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_package_installed(host: Host):
    host.run_expect([0], 'whereis podman')


def test_container_pihole_defined_and_works(host: Host):
    with host.sudo():
        host.run_expect([0], 'podman container exists pihole')
    curl_works = host.run_expect([0], "curl 'http://localhost:8091/'")
    assert 'Pi-hole: A black hole for Internet advertisements' in curl_works.stdout


def test_container_dns_works(host: Host):
    host.run_expect([0], "dig -p 8053 @127.0.0.1 google.com")


def test_container_custom_dns_works(host: Host):
    dig_out = host.run_expect([0], "dig -p 8053 @127.0.0.1 test.local.lan A +noall +answer")
    assert '10.0.0.1' in dig_out.stdout


def test_pod_pihole_defined_and_works(host: Host):
    with host.sudo():
        host.run_expect([0], 'podman pod exists test-pod-piholes')
        host.run_expect([0], 'podman container exists pihole-podded')
    curl_works = host.run_expect([0], "curl 'http://localhost:8093/'")
    assert 'Pi-hole: A black hole for Internet advertisements' in curl_works.stdout


def test_pod_dns_works(host: Host):
    host.run_expect([0], "dig -p 8054 @127.0.0.1 google.com")


def test_pod_custom_dns_works(host: Host):
    dig_out = host.run_expect([0], "dig -p 8054 @127.0.0.1 test.local.lan A +noall +answer")
    assert '10.0.0.2' in dig_out.stdout


def test_pod_httpd_container(host: Host):
    curl_works = host.run_expect([0], "curl 'http://127.0.0.1:8095/' 2>/dev/null")
    assert 'It works!' in curl_works.stdout
