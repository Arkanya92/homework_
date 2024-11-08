import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_obj = runner.Runner('Test walk')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance, 50)


    def test_run(self):
        test_obj = runner.Runner('Test run')
        for i in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    def test_challenge(self):
        test_1 = runner.Runner('run')
        test_2 = runner.Runner('walk')
        for i in range(10):
            test_1.run()
            test_2.walk()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()