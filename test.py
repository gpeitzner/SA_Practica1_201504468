import unittest

from werkzeug.wrappers import response
from app import app


class FlaskTest(unittest.TestCase):

    def test_default(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        self.assertEqual(status_code, 200)
        self.assertEqual(data, "201504468")


if __name__ == '__main__':
    unittest.main()
