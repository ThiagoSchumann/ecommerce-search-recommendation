from tests.base_test_case import BaseTestCase

class IntegrationTestCase(BaseTestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = cls.app.test_client()