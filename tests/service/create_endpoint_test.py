import unittest
import datetime

from service import create_endpoint


class TestCreateEndpoint(unittest.TestCase):

    def test_create_endpoint(self):
        date1 = datetime.date(2021, 11, 12)
        date2 = datetime.date(2021, 2, 5)
        date1_text = "/2021/11/12/"
        date2_text = "/2021/2/5/"

        title1 = "How to create an endpoint?"
        title2 = "@nak!n skywalk3r !s  the ch0sen @ne "
        title3 = " - !/.^&#"
        title1_text = "how-to-create-an-endpoint"
        title2_text = "nak-n-skywalk3r-s-the-ch0sen-ne"
        title3_text = ""

        self.assertEqual(create_endpoint(date1, title1), date1_text+title1_text)
        self.assertEqual(create_endpoint(date1, title2), date1_text+title2_text)
        self.assertEqual(create_endpoint(date2, title1), date2_text+title1_text)
        self.assertEqual(create_endpoint(date2, title2), date2_text+title2_text)
        self.assertEqual(create_endpoint(date2, title3), False)
