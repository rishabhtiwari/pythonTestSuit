import Assertions


class TestApi:
    assertObject = Assertions.Assertion()

    def __init__(self, testName, testNumber, actual=None, expected=None, responseCode=None, url=None):
        self.testName = testName
        self.url = url
        self.responseCode = responseCode
        self.actual = actual
        self.expected = expected
        self.mapper = {
            "test_upper": self.assertObject.test_upper,
            "is_upper": self.assertObject.isUpper,
            "split": self.assertObject.split,
            "response": self.assertObject.feedCallResponse
        }
        self.testNumber = testNumber

    def run(self):
        tester = self.mapper.get(self.testName.lower())
        if self.testName.lower() == "response":
            return tester(self.responseCode, self.url)
        else:
            return tester(self.actual, self.expected)
