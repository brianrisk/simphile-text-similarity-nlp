"""Utility functions for small statistical tests."""

from __future__ import annotations

from numbers import Integral
from typing import Sequence, Tuple

_EPSILON = 1e-12


def fisher_exact(table: Sequence[Sequence[int]]) -> Tuple[float, float]:
    """
    Minimal implementation of Fisher's exact test for 2x2 contingency tables.

    Returns a tuple of (odds_ratio, two_tailed_p_value) using the same defaults
    as :func:`scipy.stats.fisher_exact`.
    """
    a, b, c, d = _validate_table(table)
    odds_ratio = _compute_odds_ratio(a, b, c, d)
    p_value = _two_tailed_p_value(a, b, c, d)
    return odds_ratio, p_value


def _validate_table(table: Sequence[Sequence[int]]) -> Tuple[int, int, int, int]:
    if len(table) != 2:
        raise ValueError("fisher_exact expects a 2x2 table")
    row0, row1 = table
    if len(row0) != 2 or len(row1) != 2:
        raise ValueError("fisher_exact expects a 2x2 table")

    a, b = row0
    c, d = row1
    for value in (a, b, c, d):
        if not isinstance(value, Integral):
            raise TypeError("fisher_exact expects integer counts")
        if value < 0:
            raise ValueError("fisher_exact expects non-negative counts")

    if (a + b + c + d) == 0:
        raise ValueError("fisher_exact expects a positive total count")

    return int(a), int(b), int(c), int(d)


def _compute_odds_ratio(a: int, b: int, c: int, d: int) -> float:
    numerator = a * d
    denominator = b * c
    if denominator == 0:
        if numerator == 0:
            return float("nan")
        return float("inf")
    return numerator / denominator


def _two_tailed_p_value(a: int, b: int, c: int, d: int) -> float:
    row1 = a + b
    row2 = c + d
    col1 = a + c
    total = row1 + row2

    a_min = max(0, col1 - row2)
    a_max = min(row1, col1)
    observed_prob = _hypergeom_prob(a, row1, col1, total)

    p_value = 0.0
    for a_val in range(a_min, a_max + 1):
        prob = _hypergeom_prob(a_val, row1, col1, total)
        if prob <= observed_prob + _EPSILON:
            p_value += prob
    return min(p_value, 1.0)


def _hypergeom_prob(a: int, row1: int, col1: int, total: int) -> float:
    return (
        _comb(row1, a)
        * _comb(total - row1, col1 - a)
        / _comb(total, col1)
    )


def _comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - (k - i)) // i
    return result
