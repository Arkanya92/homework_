import unittest
import tests_12_3

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

tests = unittest.TextTestRunner(verbosity=2)
tests.run(runnerST)