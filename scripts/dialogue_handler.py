"""Emotion classification rules and face assignments for existing quotes."""

from __future__ import annotations

FACE_BY_EMOTION = {
    "surprised": "(｡⊙д⊙｡)",
    "angry": "(｡•̀へ•́｡)",
    "annoyed": "(｡•́︿•̀｡)",
    "amused": "(¬‿¬)",
    "happy": "(｡•ㅅ•｡)♡",
}

EMOTION_MARKERS = {
    "amused": ("amateur", "pathetic"),
    "angry": ("pervert", "idiot", "loser", "rude"),
    "annoyed": ("hmph", "ugh"),
    "surprised": ("w-wait", "e-eh", "!?", "huh", "eh?", "Ummm"),
    "happy": ("worked", "success", "finished", "completed", "found", "ready", "passed"),
}


def emotion_for(quote: str, exit_code: int) -> str:
    """Assign an emotion to an existing command quote without changing it."""
    lowered_quote = quote.lower()
    for emotion in ("amused", "angry", "annoyed", "surprised", "happy"):
        if any(marker in lowered_quote for marker in EMOTION_MARKERS[emotion]):
            return emotion
    return "happy" if exit_code == 0 else "angry"
