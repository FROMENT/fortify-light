import unittest
from scripts.extract_metrics import extract_metrics

class TestExtractMetrics(unittest.TestCase):

    def test_extract_metrics(self):
        csv_file = 'data/vulnerabilities.csv'  # Ensure this file exists for the test
        metrics = extract_metrics(csv_file)
        self.assertIsNotNone(metrics)
        self.assertIsInstance(metrics, dict)
        self.assertIn('categories', metrics)
        self.assertIn('severities', metrics)
        self.assertIn('files', metrics)
        self.assertIn('audit_status', metrics)
        self.assertIn('total_vulnerabilities', metrics)

if __name__ == '__main__':
    unittest.main()