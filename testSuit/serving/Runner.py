import TestingApi
import concurrent.futures
import datetime
import time
import random


class Runner:
    taskList = []

    def __init__(self, testExecutionChart, workers):
        self.testExecutionChart = testExecutionChart
        self.totalTestCases = len(self.testExecutionChart)
        self.workers = workers

    def start(self):
        for (i, test) in zip(range(0, len(self.testExecutionChart)), self.testExecutionChart):
            if test[0].lower() == "response":
                task = TestingApi.TestApi(test[0], i, responseCode=test[1], url=test[2])
                self.taskList.append(task)
            else:
                task = TestingApi.TestApi(test[0], i, actual=test[1], expected=test[2])
                self.taskList.append(task)

        with concurrent.futures.ThreadPoolExecutor(self.workers) as executor:
            future_to_testName = {executor.submit(task.run): task.testNumber for task in self.taskList}
            for future in concurrent.futures.as_completed(future_to_testName):
                testName = future_to_testName[future]
                try:
                    isPassed = future.result()
                except Exception as ex:
                    print('Test Case {} Failed Exception {}'.format(testName, ex.args))
                else:
                    print('Test Case {} Passed'.format(testName))
        return "ok"


if __name__ == '__main__':
    currentTimeInMs = int(time.time() * 1000)
    mapper = {
        0: ["response", 200,
            "http://www.python.org/"],
        1: ["test_upper", "RISHABH", "RISHABH"],
        2: ["is_upper", "rishabh", "RISHABH"],
        3: ["split", "one,two,three", ['one', 'two', 'three']]
    }
    testList = [mapper.get(random.randint(0, len(mapper) - 1)) for i in range(0, 100)]
    testSuitRunner = Runner(testList, 10)
    testSuitRunner.start()
    print('process finished at time {}'.format(datetime.datetime.now()))
    print('Total Time to Complete the process {}'.format(int(time.time() * 1000) - currentTimeInMs))
