import unittest
import io
from unittest.mock import patch, Mock
from handlers.get_handler import get_selected,get_all
from utils import get_error_response
from test_utils import MockRequest


class Test_Get_Handler(unittest.TestCase):
    def test_get_all(self):
        # Mock the behavior of db_helper
        cat_pictures_data = ["pic1",
                            "pic2"]
        mock_db_helper = Mock()
        mock_db_helper.get.return_value = cat_pictures_data

        response = get_all(mock_db_helper,"test")
        print("hello response",response)
        self.assertEqual(response["cat_pictures"],cat_pictures_data)

