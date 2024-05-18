#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to calculate start and end indexes
    for pagination.

    @page: integer, the page number (1-indexed)
    @page_size: integer, number of items per page
    Returns: tuple, containing start and end indexes
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    
    return (start_index, end_index)
