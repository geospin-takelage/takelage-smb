import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_root_bashrc_file(host, testvars):
    with host.sudo():
        file = host.file('/root/.bashrc')

        assert file.exists
        assert file.is_file
        assert file.user == 'root'
        assert file.group == 'root'
        assert file.mode == 0o644


def test_takel_root_bashrc_directory(host, testvars):
    with host.sudo():
        dir = host.file('/root/.bashrc.d')

        assert dir.exists
        assert dir.is_directory
        assert dir.user == 'root'
        assert dir.group == 'root'
        assert dir.mode == 0o755


def test_takel_root_bashrc_files(host, testvars):
    bashrc_files = testvars['takel_root_bashrc']
    for bashrc_file in bashrc_files:
        with host.sudo():
            file = host.file('/root/.bashrc.d/' +
                             str(bashrc_file['order']) +
                             bashrc_file['file'])
            assert file.exists
            assert file.is_file
            assert file.user == 'root'
            assert file.group == 'root'
            assert file.mode == 0o644
