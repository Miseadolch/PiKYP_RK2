import unittest
from main import get_one_to_many, get_many_to_many, task_G1, task_G2, task_G3, catalogs, files, files_in_catalog

class TestFileCatalog(unittest.TestCase):

    def setUp(self):
        """Set up the one-to-many and many-to-many relationships for testing."""
        self.one_to_many = get_one_to_many(catalogs, files)
        self.many_to_many = get_many_to_many(catalogs, files, files_in_catalog)

    def test_task_G1(self):
        """Test task_G1 for finding files in catalogs starting with 'A'."""
        expected_result = [('Сумма закупки', 500, 'Аспирантские закупки'),
                           ('Руководитель закупки', 320, 'Аспирантские закупки')]
        self.assertEqual(task_G1(self.one_to_many), expected_result)

    def test_task_G2(self):
        """Test task_G2 for finding the largest file in each catalog."""
        expected_result = [('Закупки для офиса', 550),
                           ('Аспирантские закупки', 500),
                           ('Закупки для университета', 490),
                           ('Закупки для партнеров', 120)]
        self.assertEqual(task_G2(catalogs, self.one_to_many), expected_result)

    def test_task_G3(self):
        """Test task_G3 for listing all files by catalog."""
        expected_result = {
            'Аспирантские закупки': ['Сумма закупки', 'Руководитель закупки'],
            'Закупки для университета': ['Номер контрактов'],
            'Закупки для офиса': ['Поставщики'],
            'Закупки для партнеров': ['Юр. данные']
        }
        self.assertEqual(task_G3(catalogs, self.many_to_many), expected_result)

if __name__ == '__main__':
    unittest.main()
