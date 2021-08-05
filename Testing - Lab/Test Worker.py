class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_initializing(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_increment_on_worker_energy(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_error_for_no_energy_worker(self):
        worker = Worker("TestGuy", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_salary_increase_after_work(self):
        expected_money = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)

    def test_energy_decrease_after_work(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_method_return(self):
        expected = f"{self.worker.name} has saved {self.worker.money} money."
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
