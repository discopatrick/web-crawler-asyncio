from unittest import TestCase

from web_crawler import get_html_from_url


class WebCrawlerTest(TestCase):

    def test_get_example_com(self):
        html = get_html_from_url('http://example.com')
        self.assertIn('<h1>Example Domain</h1>', html)
