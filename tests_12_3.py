import module_12_1
import module_12_2
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tmp = module_12_1.Runner('Denis')
        for i in range(10):
            tmp.walk()
        self.assertEqual(tmp.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tmp = module_12_1.Runner('Denis')
        for i in range(10):
            tmp.run()
        self.assertEqual(tmp.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tmp1 = module_12_1.Runner('Denis')
        tmp2 = module_12_1.Runner('Jane')
        for i in range(10):
            tmp1.run()
            tmp2.walk()
        self.assertNotEqual(tmp1.distance, tmp2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = module_12_2.Runner('Усэйн', 10)
        self.second = module_12_2.Runner('Андрей', 9)
        self.third = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start(self):
        pair1 = module_12_2.Tournament(90, self.first, self.third)
        for k, v in pair1.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        pair2 = module_12_2.Tournament(90, self.second, self.third)
        for k, v in pair2.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        pair3 = module_12_2.Tournament(90, self.first, self.second, self.third)
        for k, v in pair3.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[3])


if __name__ == '__main__':
    unittest.main()
