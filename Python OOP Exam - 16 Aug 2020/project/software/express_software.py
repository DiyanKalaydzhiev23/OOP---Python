from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))

