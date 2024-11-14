import logging
import unittest
import module_12_4


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            tmp = module_12_4.Runner('Denis', -10)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                tmp.walk()
            self.assertEqual(tmp.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            tmp = module_12_4.Runner(123)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                tmp.run()
            self.assertEqual(tmp.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skip
    def test_challenge(self):
        tmp1 = module_12_4.Runner('Denis')
        tmp2 = module_12_4.Runner('Jane')
        for i in range(10):
            tmp1.run()
            tmp2.walk()
        self.assertNotEqual(tmp1.distance, tmp2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()
