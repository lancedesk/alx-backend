#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""
from typing import List, Tuple
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to calculate start and end indexes
    for pagination.

    @page: integer, the page number (1-indexed)
    @page_size: integer, number of items per page
    Returns: tuple, containing start and end indexes
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        @page: integer, the page number (1-indexed)
        @page_size: integer, number of items per page
        Returns: list of lists, the paginated data
        """

        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the dataset with hypermedia information.

        @page: integer, the page number (1-indexed)
        @page_size: integer, number of items per page
        Returns: dict, containing the paginated data and hypermedia info
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hypermedia_info = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hypermedia_info
