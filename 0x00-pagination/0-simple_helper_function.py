#!/usr/bin/env python3
"""Task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing
    a start index and an end index corresponding to
    the range of indexes to return in a list for those
    particular pagination parameters."""
    first = (page - 1) * page_size
    return (first, first + page_size)
