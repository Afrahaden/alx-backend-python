#!/usr/bin/env python3
""" Parameterize a unit test, Mock HTTP calls """
""" Parameterize a unit test, Mock HTTP calls, Parameterize and patch """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)