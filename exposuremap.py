"""Helpers for defensive exposure inventories."""

def normalize(asset: dict) -> dict:
    return {"host": str(asset.get("host", "")).strip().lower(), "service": str(asset.get("service", "")).strip().lower(), "exposed": bool(asset.get("exposed", False))}


def group_by_host(assets):
    result = {}
    for asset in assets:
        item = normalize(asset)
        result.setdefault(item["host"], []).append(item)
    return result


def exposed_hosts(assets):
    return sorted({normalize(a)["host"] for a in assets if normalize(a)["exposed"]})
