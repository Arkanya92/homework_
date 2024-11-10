import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        self.participants.sort(key=lambda x: x.speed, reverse=True)  # Сортировка скорости по уменьшению.
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print({k: v.name for k, v in cls.all_results[key].items()})

    def test_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()

        self.__class__.all_results[1] = result

        max_key = len(result)
        self.assertEqual(str(result[max_key]), "Ник")

    def test_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()

        self.__class__.all_results[2] = result

        max_key = len(result)
        self.assertEqual(str(result[max_key]), "Ник")

    def test_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()

        self.__class__.all_results[3] = result

        max_key = len(result)
        self.assertEqual(str(result[max_key]), "Ник")

    def test_4(self):
        tournament = Tournament(3, self.runner_3, self.runner_1)
        result = tournament.start()

        self.__class__.all_results[4] = result

        max_key = len(result)
        self.assertEqual(str(result[max_key]), "Ник")


if __name__ == "__main__":
    unittest.main()
