from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class FileUploadTestCase(APITestCase):
    def test_upload_file(self):
        # Prepare a file for upload
        file_content = b'This is a test file.'
        test_file = SimpleUploadedFile("testfile.txt", file_content, content_type="text/plain")

        # Perform the POST request
        response = self.client.post(
            "http://127.0.0.1:8000/project/api/projects/documents/upload/",  # Replace with your upload URL
            {"file": test_file},  # Pass the file in the request
            format="multipart"  # Important: Specify multipart format
        )

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Adjust expected status code
        self.assertIn("detail", response.data)  # Adjust the assertion as needed
        self.assertEqual(response.data["detail"], "File uploaded successfully.")  # Match expected response
