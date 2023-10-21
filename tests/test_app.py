import unittest
from unittest.mock import patch, Mock
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.post_handler.post_cat_pic')
    def test_upload_cat_picture(self, mock_post_cat_pic):
        test_response = "Mock Post successful"
        mock_post_cat_pic.return_value = test_response
        response = self.app.post('/upload')
        self.assertEqual(response.status_code, 200)
        mock_post_cat_pic.assert_called_once()

    @patch('app.get_handler.get_all')
    def test_get_cat_pictures(self, mock_get_all):
        mock_get_all.return_value = "Test get all"
        response = self.app.get('/get')
        self.assertEqual(response.status_code, 200)
        mock_get_all.assert_called_once()

    @patch('app.get_handler.get_selected')
    def test_get_cat_picture(self, mock_get_selected):
        mock_get_selected.return_value = "Test Get Selected"
        response = self.app.get('/get/1')
        self.assertEqual(response.status_code, 200)
        mock_get_selected.assert_called_once()

    @patch('app.put_handler.update_pic')
    def test_update_cat_picture(self, mock_update_pic):
        mock_update_pic.return_value = "Test Put"
        response = self.app.put('/update/1')
        self.assertEqual(response.status_code, 200)
        mock_update_pic.assert_called_once()

    @patch('app.delete_handler.delete_pic')
    def test_delete_cat_picture(self, mock_delete_pic):
        mock_delete_pic.return_value = "Test delete"
        response = self.app.delete('/delete/1')
        self.assertEqual(response.status_code, 200)
        mock_delete_pic.assert_called_once()

if __name__ == '__main__':
    unittest.main()
