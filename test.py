from application.utility import *
import pandas as pd
import unittest
import requests
import random
import subprocess


class EnrichSeq(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_EnrichSeq_results(self):
        num_phages = 20
        timesteps = 10
        std_error = 10
        df = generate_EnrichSeq_results("12345", num_phages, timesteps)
        self.assertEqual(df["reads"].count(), num_phages*timesteps)

if __name__ == '__main__':
    unittest.main()