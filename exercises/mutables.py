"""
Examples demonstrating mutable default argument pitfalls and safe patterns.
Each "bad_*" function shows the surprising shared-state behavior.
Each corresponding "safe_*" function uses None/default_factory pattern to avoid it.
"""
from __future__ import annotations
from typing import Any


def bad_append(value: Any, lst: list = []):
    """Appends value to a default list (shared between calls)."""
    lst.append(value)
    return lst


def safe_append(value: Any, lst: list | None = None):
    """Safe version: creates a new list when lst is None."""
    if lst is None:
        lst = []
    lst.append(value)
    return lst


def bad_count(name: str, counts: dict = {}):
    """Accumulates counts in a default dict (shared)."""
    counts[name] = counts.get(name, 0) + 1
    return counts


def safe_count(name: str, counts: dict | None = None):
    """Safe version that uses a fresh dict when None."""
    if counts is None:
        counts = {}
    counts[name] = counts.get(name, 0) + 1
    return counts


def bad_collect(item: Any, bucket: list = []):
    """Collects items into a default list (shared)."""
    bucket.append(item)
    return bucket


def safe_collect(item: Any, bucket: list | None = None):
    """Safe collector that avoids shared default list."""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def bad_register(callback: Any, callbacks: list = []):
    """Registers callbacks into a shared default list."""
    callbacks.append(callback)
    return callbacks


def safe_register(callback: Any, callbacks: list | None = None):
    """Safe register that creates a new list per call if needed."""
    if callbacks is None:
        callbacks = []
    callbacks.append(callback)
    return callbacks
