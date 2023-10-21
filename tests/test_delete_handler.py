import unittest
from unittest.mock import Mock
from handlers.delete_handler import delete_pic

class TestDeletePic(unittest.TestCase):

    def test_delete_pic_with_existing_id(self):
        db_helper = Mock()
        cat_data = {'cat_id': 1, 'name': 'Fluffy'}
        db_helper.get.return_value = cat_data
        db_helper.delete.return_value = True

        response = delete_pic(db_helper, 'test', 1)

        self.assertEqual(response, "Cat picture deleted successfully")

    def test_delete_pic_with_non_existing_id(self):
        db_helper = Mock()
        db_helper.get.return_value = None

        response = delete_pic(db_helper, 'test', 2)

        self.assertEqual(response.status_code, 404)

    def test_delete_pic_with_error_deleting_image(self):
        db_helper = Mock()
        cat_data = {'cat_id': 1, 'name': 'Fluffy'}
        db_helper.get.return_value = cat_data
        db_helper.delete.return_value = False

        response = delete_pic(db_helper, 'test', 1)

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
