import unittest
import requests
import http.client
http.client._MAXHEADERS = 1000


class Assertion(unittest.TestCase):

    def __init__(self):
        super().__init__()

    def test_upper(self, actual, expected):
        if actual is None or expected is None:
            self.fail("test_upper Failed due to Empty actual {} and expected {}".format(actual,expected))
        self.assertEqual(actual, expected, "test_upper Failed")

    def isUpper(self, actual, expected):
        if actual is None or expected is None:
            self.fail("is_upper Failed due to Empty actual {} and expected {}".format(actual,expected))
        self.assertEquals(actual.upper(), expected, "is_upper Failed")

    def split(self, actual, expected):
        if actual is None or expected is None:
            self.fail("split Failed due to Empty actual {} and expected {}".format(actual,expected))
        self.assertEqual(actual.split(","),expected, "Split Failed")

    def feedCallResponse(self, expected, url="www.python.org"):
        try:
            print ("Establishing Connection With URL: {}".format(url))
            response = requests.get(url=url)
            print ('responseStatus: {}'.format(response.status_code))
            self.assertEqual(response.status_code, expected, "Feed Response Failed")
        except Exception as ex:
            self.fail("response code expected {} but found null\n + {}".format(expected,ex.args))