"""
mark_for_deletion.py - Mark for Deletion object

Provides a class model for the FR API Mark for Deletion(tm) object

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.md
"""
from functools import reduce
from operator import xor
from typing import Optional


class MarkForDeletion(object):
    """
    Data object representing a MD structurefrom the API
    """

    def __init__(self, marked: bool = False, reporter: Optional[str] = None,
                 reason: Optional[str] = None):
        """
        Creates a new MD object

        Args:
            marked (bool): Indicates whether the object is marked for deletion
            reason (str): Reported reason for deleting the Rescue
            reporter (str): IRC nickname of the user that marked the case for deletion
        """
        self._reporter = reporter
        self._marked = marked
        self._reason = reason
        self._hash = None

    def __eq__(self, other: 'MarkForDeletion') -> bool:
        if not isinstance(other, MarkForDeletion):
            return NotImplemented

        conditions = (
            self.reason == other.reason,
            self.reporter == other.reporter,
            self.marked == other.marked
        )
        return all(conditions)

    def __hash__(self):

        if self._hash is None:
            attributes = (
                self.marked,
                self.reason,
                self.reporter
            )

            self._hash = reduce(xor, map(hash, attributes))
        return self._hash

    @property
    def marked(self) -> bool:
        """
        Marker indicating whether the Rescue is marked for deletion

        Returns:
            bool
        """
        return self._marked

    @marked.setter
    def marked(self, value: bool) -> None:
        """
        Set the MD status

        Args:
            value (bool): MD status

        Returns:
            None

        Raises:
            TypeError: invalid type
        """
        if isinstance(value, bool):
            self._marked = value
        else:
            raise TypeError

    @property
    def reason(self) -> Optional[str]:
        """
        Reported reason for marking the case as deleted

        Returns:
            str: reported reason
        """
        return self._reason

    @reason.setter
    def reason(self, value: Optional[str]) -> None:
        """
        Set the MD reason

        Args:
            value (str): MD reason string

        Returns:
            None

        Raises:
            TypeError: invalid type
        """
        if isinstance(value, str) or value is None:
            self._reason = value
        else:
            raise TypeError

    @property
    def reporter(self) -> Optional[str]:
        """
        IRC nickname of reporting user

        Returns:
            str: string nickname
        """
        return self._reporter

    @reporter.setter
    def reporter(self, value: Optional[str]) -> None:
        """
        Sets the reporter

        Args:
            value (str): reporters nickname

        Returns:
            None

        Raises:
            TypeError: invalid type
        """
        if isinstance(value, str) or value is None:
            self._reporter = value
        else:
            raise TypeError
