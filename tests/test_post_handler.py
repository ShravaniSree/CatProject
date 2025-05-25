import unittest
from unittest.mock import Mock
from ..handlers.post_handler import post_cat_pic

class TestPostCatPic(unittest.TestCase):

    def test_post_cat_pic_with_valid_file(self):
        db_helper = Mock()
        request = Mock()
        request.files = {'file': Mock(filename='cat.jpg', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = None
        db_helper.add.return_value = None

        response = post_cat_pic(db_helper, Mock(), request)

        self.assertEqual(response, "Cat picture uploaded successfully")

    def test_post_cat_pic_with_existing_id(self):
        db_helper = Mock()
        request = Mock()
        request.files = {'file': Mock(filename='cat.jpg', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = {'cat_id': 1}

        response = post_cat_pic(db_helper, 'test', request)

        self.assertEqual(response.status_code, 409)

    def test_post_cat_pic_with_no_image_provided(self):
        db_helper = Mock()
        request = Mock()
        request.files = None

        response = post_cat_pic(db_helper, 'test', request)

        self.assertEqual(response.status_code, 400)

    def test_post_cat_pic_with_invalid_file_extension(self):
        db_helper = Mock()
        request = Mock()
        request.files = {'file': Mock(filename='cat.txt', read=lambda: b'fake_image_data')}
        db_helper.get.return_value = None

        response = post_cat_pic(db_helper, 'test', request)

        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
