import pytest

def test_vector_installed(host):
    vector = host.package("vector")
    assert vector.is_installed

@pytest.mark.parametrize("service_name", ["vector"])
def test_vector_service(host, service_name):
    if host.system_info.distribution.lower() in ["oracle", "centos", "redhat"]:
        service = host.service(service_name)
        assert service.is_enabled
        assert service.is_running
    else:
        # На Ubuntu без systemd пропускаем проверку сервиса
        pass
