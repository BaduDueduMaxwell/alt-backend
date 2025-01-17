#!/usr/bin/env python3
"""
Added a method called `get_page`
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows for the specified page, or
            an empty list if page and page_size are out of range.
        """

        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = self.index_range(page, page_size)

        dataset = self.dataset()
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
