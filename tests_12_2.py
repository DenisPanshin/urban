import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.first = module_12_2.Runner('Усэйн', 10)
        self.second = module_12_2.Runner('Андрей', 9)
        self.third = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def test_start(self):
        pair1 = module_12_2.Tournament(90, self.first, self.third)
        for k, v in pair1.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[2])

    def test_start2(self):
        pair2 = module_12_2.Tournament(90, self.second, self.third)
        for k, v in pair2.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[2])

    def test_start3(self):
        pair3 = module_12_2.Tournament(90, self.first, self.second, self.third)
        for k, v in pair3.start().items():
            TournamentTest.all_results.update({k: str(v)})

        self.assertTrue(self.third.name == TournamentTest.all_results[3])


if __name__ == '__main__':
    unittest.main()
