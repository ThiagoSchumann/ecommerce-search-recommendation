import unittest

from main import Application

class BaseTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        application = Application()
        cls.app = application.http_server.app
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()