#!/usr/bin/env python3
"""Defines the index_range function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size
    in a paginated list.

    Parameters:
    - page (int): The page number (1-based index).
    - page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start index and end index
    for the specified page in the paginated list.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)
