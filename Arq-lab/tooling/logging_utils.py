from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from typing import Any


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def log_event(event: str, **fields: Any) -> None:
    record = {"ts": utc_timestamp(), "event": event, **fields}
    print(json.dumps(record, sort_keys=True, ensure_ascii=True), file=sys.stdout, flush=True)

