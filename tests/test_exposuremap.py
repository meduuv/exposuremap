from exposuremap import group_by_host, exposed_hosts


def test_group_and_exposed():
    items = [{"host": "WEB.EXAMPLE", "service": "HTTPS", "exposed": True}, {"host": "web.example", "service": "ssh", "exposed": False}]
    assert len(group_by_host(items)["web.example"]) == 2
    assert exposed_hosts(items) == ["web.example"]
