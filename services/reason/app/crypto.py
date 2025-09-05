import hashlib
import orjson


def sha256(payload) -> str:
    if not isinstance(payload, (bytes, bytearray)):
        payload = orjson.dumps(payload)
    return hashlib.sha256(payload).hexdigest()
