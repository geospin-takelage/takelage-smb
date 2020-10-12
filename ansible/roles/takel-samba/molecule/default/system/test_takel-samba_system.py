import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_samba_system_smbclient_connect_to_smbd(host):
    command = 'smbclient --no-pass --list=127.0.0.1'
    assert host.run_expect([0], command)
