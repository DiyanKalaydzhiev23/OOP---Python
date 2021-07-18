class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity - len(self.workers) > 0:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0

        for worker in self.workers:
            salaries += worker.salary

        if self.__budget - salaries >= 0:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending = 0

        for animal in self.animals:
            tending += animal.money_for_care

        if self.__budget - tending >= 0:
            self.__budget -= tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_lions = 0
        total_tigers = 0
        total_cheetahs = 0

        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                total_lions += 1
                lions.append(animal)
            elif type(animal).__name__ == "Tiger":
                total_tigers += 1
                tigers.append(animal)
            elif type(animal).__name__ == "Cheetah":
                total_cheetahs += 1
                cheetahs.append(animal)

        lions_info = '\n'.join(str(lion) for lion in lions)
        tigers_info = '\n'.join(str(tiger) for tiger in tigers)
        cheetahs_info = '\n'.join(str(cheetah) for cheetah in cheetahs)

        return f"You have {len(self.animals)} animals\n----- {len(lions)} " \
               f"Lions:\n{lions_info}\n----- {len(tigers)} Tigers:\n" \
               f"{tigers_info}\n----- {len(cheetahs)} Cheetahs:\n{cheetahs_info}"

    def workers_status(self):
        total_caretakers = 0
        total_keepers = 0
        total_vets = 0

        caretakers = []
        keepers = []
        vets = []

        for worker in self.workers:
            if type(worker).__name__ == "Caretaker":
                total_caretakers += 1
                caretakers.append(worker)
            elif type(worker).__name__ == "Keeper":
                total_keepers += 1
                keepers.append(worker)
            elif type(worker).__name__ == "Vet":
                total_vets += 1
                vets.append(worker)

        caretakers_info = '\n'.join(str(caretaker) for caretaker in caretakers)
        keepers_info = '\n'.join(str(keeper) for keeper in keepers)
        vets_info = '\n'.join(str(vet) for vet in vets)

        return f"You have {len(self.workers)} workers\n----- {len(keepers)} " \
               f"Keepers:\n{keepers_info}\n----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_info}\n----- {len(vets)} Vets:\n{vets_info}"
