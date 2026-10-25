"""Read-only NVDA scratchpad plug-in for the isolated screen-reader check.

Records NVDA's real pre-synthesis output, never generates announcements.
Only the explicitly selected browser process and application title are accepted.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import api
import globalPluginHandler
from speech.extensions import pre_speech


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()
        self.base = Path(__file__).parents[2]
        pre_speech.register(self.record)
        self.base.joinpath("ready.json").write_text('{"ready":true}', encoding="utf-8")

    def record(self, speechSequence, **kwargs):
        try:
            target = json.loads(self.base.joinpath("target.json").read_text(encoding="utf-8"))
            foreground = api.getForegroundObject()
            if foreground.processID != target["pid"] or "EcoLogística" not in (foreground.name or ""):
                return
            text = " ".join(item for item in speechSequence if isinstance(item, str))
            if not text or not target.get("step"):
                return
            event = {"at": datetime.now(timezone.utc).isoformat(), "step": target["step"], "text": text}
            with self.base.joinpath("speech.jsonl").open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(event, ensure_ascii=False) + "\n")
        except (OSError, ValueError, AttributeError):
            # A missing target file during startup/cleanup must not affect NVDA.
            return

    def terminate(self):
        pre_speech.unregister(self.record)
        super().terminate()
