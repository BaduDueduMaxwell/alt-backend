#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index
    for the items on a specific page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of (start_index, end_index) representing
        the range of indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
