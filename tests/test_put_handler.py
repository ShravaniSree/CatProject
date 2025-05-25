import unittest
from unittest.mock import Mock
from .test_utils import MockRequest
from ..handlers.put_handler import update_pic

class TestUpdatePic(unittest.TestCase):

    def test_update_pic_with_existing_id_and_valid_file(self):
        db_helper = Mock()
        cat_data = MockRequest("test","test")
        request = Mock()
        request.files = {'file': Mock(filename='cat.jpg', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = cat_data
        db_helper.db.session.commit.return_value = None

        response = update_pic(db_helper, 'test', request, 1)

        self.assertEqual(response, "Cat picture updated successfully")

    def test_update_pic_with_non_existing_id(self):
        db_helper = Mock()
        request = Mock()
        request.files = {'file': Mock(filename='cat.jpg', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = None

        response = update_pic(db_helper, 'test', request, 2)

        self.assertEqual(response.status_code, 404)

    def test_update_pic_with_no_image_provided(self):
        db_helper = Mock()
        request = Mock()
        request.files = None

        response = update_pic(db_helper, 'test', request, 1)

        self.assertEqual(response.status_code, 400)

    def test_update_pic_with_invalid_file_extension(self):
        db_helper = Mock()
        cat_data = {'cat_id': 1}
        request = Mock()
        request.files = {'file': Mock(filename='cat.txt', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = cat_data

        response = update_pic(db_helper, 'test', request, 1)

        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
