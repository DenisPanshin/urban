import module_12_1
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        tmp = module_12_1.Runner('Denis')
        for i in range(10):
            tmp.walk()
        self.assertEqual(tmp.distance, 50)

    def test_run(self):
        tmp = module_12_1.Runner('Denis')
        for i in range(10):
            tmp.run()
        self.assertEqual(tmp.distance, 100)

    def test_challenge(self):
        tmp1 = module_12_1.Runner('Denis')
        tmp2 = module_12_1.Runner('Jane')
        for i in range(10):
            tmp1.run()
            tmp2.walk()
        self.assertNotEqual(tmp1.distance, tmp2.distance)


if __name__ == '__main__':
    unittest.main()
