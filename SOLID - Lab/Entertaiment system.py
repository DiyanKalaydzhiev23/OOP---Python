class HdmiConnection:
    def connect_to_device_via_hdmi_cable(self, device): pass


class RcaConnection:
    def connect_to_device_via_rca_cable(self, device): pass


class EthernetConnection:
    def connect_to_device_via_ethernet_cable(self, device): pass


class PowerOutletConnection:
    def connect_device_to_power_outlet(self, device): pass


class Television(RcaConnection, HdmiConnection, PowerOutletConnection):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HdmiConnection, PowerOutletConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HdmiConnection, EthernetConnection, PowerOutletConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetConnection, PowerOutletConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
