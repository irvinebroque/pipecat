#
# Copyright (c) 2024-2026, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

"""RTVI (Real-Time Voice Interface) protocol implementation for Pipecat."""

from importlib import import_module

__all__ = [
    "BotOutputTransformResult",
    "SpokenProgressData",
    "RTVIClientMessageFrame",
    "RTVIFunctionCallReportLevel",
    "RTVIObserver",
    "RTVIObserverParams",
    "RTVIProcessor",
    "RTVIServerMessageFrame",
    "RTVIServerResponseFrame",
    "RTVIUICancelJobGroupFrame",
    "RTVIUICommandFrame",
    "RTVIUIEventFrame",
    "RTVIUISnapshotFrame",
    "RTVIUIJobGroupFrame",
]


_LAZY_EXPORTS = {
    "BotOutputTransformResult": ".models",
    "SpokenProgressData": ".models",
    "RTVIClientMessageFrame": ".frames",
    "RTVIFunctionCallReportLevel": ".observer",
    "RTVIObserver": ".observer",
    "RTVIObserverParams": ".observer",
    "RTVIProcessor": ".processor",
    "RTVIServerMessageFrame": ".frames",
    "RTVIServerResponseFrame": ".frames",
    "RTVIUICancelJobGroupFrame": ".frames",
    "RTVIUICommandFrame": ".frames",
    "RTVIUIEventFrame": ".frames",
    "RTVIUISnapshotFrame": ".frames",
    "RTVIUIJobGroupFrame": ".frames",
}


def __getattr__(name: str):
    module = _LAZY_EXPORTS.get(name)
    if module is None:
        raise AttributeError(name)
    value = getattr(import_module(module, __name__), name)
    globals()[name] = value
    return value
