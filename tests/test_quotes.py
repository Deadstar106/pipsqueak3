"""
rat_rescue.py - Rescue board and objects

Copyright (c) 2018 The Fuel Rats Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.md

This module is built on top of the Pydle system.
"""
from unittest import TestCase, expectedFailure

from Modules.rat_rescue import Quotes



class TestQuotes(TestCase):

    def setUp(self):
        pass

    def test_message(self):
        expectedMessage = "some test message"
        quote = Quotes(message=expectedMessage)
        self.assertEqual(expectedMessage, quote.message)

    def test_message_setter(self):
        self.fail()

    def test_author(self):
        self.fail()

    def test_created_at(self):
        self.fail()

    def test_updated_at(self):
        self.fail()

    def test_updated_at_setter(self):
        self.fail()

    def test_last_author(self):
        self.fail()

    def test_last_author_setter(self):
        self.fail()

    def test_modify(self):
        self.fail()

    def test_new(self):
        self.fail()