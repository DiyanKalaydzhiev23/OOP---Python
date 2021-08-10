from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(express_software)
            System._software.append(express_software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(light_software)
            System._software.append(light_software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            software = [s for s in System._software if s.name == software_name][0]
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        used_memory = sum([s.memory_consumption for s in System._software])
        total_capacity = sum([h.capacity for h in System._hardware])
        used_capacity = sum([s.capacity_consumption for s in System._software])
        return "System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}\n")
            result.append(f"Express Software Components: {System.count_components(hardware, 'Express')}\n")
            result.append(f"Light Software Components: {System.count_components(hardware, 'Light')}\n")
            result.append(f"Memory Usage: {System.memory_usage(hardware)}\n")
            result.append(f"Capacity Usage: {System.capacity_usage(hardware)}\n")
            result.append(f"Type: {hardware.type}\n")
            result.append(f"Software Components: {System.get_software_components_names(hardware)}")
        return ''.join(result)

    @staticmethod
    def get_software_components_names(hardware):
        names = [s.name for s in hardware.software_components]
        if not names:
            return None
        return ', '.join(names)

    @staticmethod
    def memory_usage(hardware):
        used_memory = sum([s.memory_consumption for s in hardware.software_components])
        return f"{used_memory} / {hardware.memory}"

    @staticmethod
    def capacity_usage(hardware):
        used_capacity = sum([s.capacity_consumption for s in hardware.software_components])
        return f"{used_capacity} / {hardware.capacity}"

    @staticmethod
    def count_components(hardware, searched_type):
        return len([s for s in hardware.software_components if s.type == searched_type])
