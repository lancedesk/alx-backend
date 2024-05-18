#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page from the dataset with hypermedia information.

        @index: integer, the start index of the return page
        @page_size: integer, number of items per page
        Returns: dict, containing the paginated data and hypermedia info
        """

        assert index is not None and isinstance(index, int) and index >= 0
        assert page_size > 0 and isinstance(page_size, int)

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index < total_items

        data = []
        next_index = index
        count = 0

        while count < page_size and next_index < total_items:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                count += 1
            next_index += 1

        next_index = next_index if next_index < total_items else None
        prev_index = index - page_size if index - page_size >= 0 else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
            'prev_index': prev_index
        }
