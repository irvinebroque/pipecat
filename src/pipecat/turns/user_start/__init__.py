#
# Copyright (c) 2024-2026, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

from importlib import import_module

__all__ = [
    "BaseUserTurnStartStrategy",
    "ExternalUserTurnStartStrategy",
    "KrispVivaIPUserTurnStartStrategy",
    "MinWordsUserTurnStartStrategy",
    "TranscriptionUserTurnStartStrategy",
    "UserTurnStartedParams",
    "VADUserTurnStartStrategy",
    "WakePhraseUserTurnStartStrategy",
]


_LAZY_EXPORTS = {
    "BaseUserTurnStartStrategy": ".base_user_turn_start_strategy",
    "UserTurnStartedParams": ".base_user_turn_start_strategy",
    "ExternalUserTurnStartStrategy": ".external_user_turn_start_strategy",
    "MinWordsUserTurnStartStrategy": ".min_words_user_turn_start_strategy",
    "TranscriptionUserTurnStartStrategy": ".transcription_user_turn_start_strategy",
    "VADUserTurnStartStrategy": ".vad_user_turn_start_strategy",
    "WakePhraseUserTurnStartStrategy": ".wake_phrase_user_turn_start_strategy",
    "KrispVivaIPUserTurnStartStrategy": ".krisp_viva_ip_user_turn_start_strategy",
}


def __getattr__(name: str):
    module = _LAZY_EXPORTS.get(name)
    if module is None:
        raise AttributeError(name)
    try:
        value = getattr(import_module(module, __name__), name)
    except ImportError:
        if name != "KrispVivaIPUserTurnStartStrategy":
            raise
        value = None
    globals()[name] = value
    return value
