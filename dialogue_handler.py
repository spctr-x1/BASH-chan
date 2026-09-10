"""Emotion classification rules and face assignments for existing quotes."""

from __future__ import annotations

FACE_BY_EMOTION = {
    "surprised": "(｡⊙д⊙｡)",
    "angry": "(｡•̀へ•́｡)",
    "annoyed": "(｡•́︿•̀｡)",
    "happy": "(｡•ㅅ•｡)♡",
    "sad": "(｡•́︿•̀｡)｡",
}

EMOTION_MARKERS = {
    "angry": ("pervert", "idiot", "loser", "rude"),
    "annoyed": ("hmph", "ugh"),
    "surprised": ("w-wait", "e-eh", "!?", "huh", "eh?"),
    "happy": ("worked", "success", "finished", "completed", "found", "ready", "passed"),
    "sad": ("failed", "couldn't", "could not", "refused", "rejected", "wrong", "disappointing", "nothing"),
}


def emotion_for(quote: str, exit_code: int) -> str:
    """Assign an emotion to an existing command quote without changing it."""
    lowered_quote = quote.lower()
    for emotion in ("angry", "annoyed", "surprised", "sad", "happy"):
        if any(marker in lowered_quote for marker in EMOTION_MARKERS[emotion]):
            return emotion
    if exit_code != 0:
        return "sad"
    return "happy"
