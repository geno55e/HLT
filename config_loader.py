import configparser


class Config:
    def __init__(self, config_path: str = "config.ini"):
        self.config_path = config_path
        self.address_power_source = None
        self.address_frequency_generator = None
        self.address_multimeter = None
        self.step_size_pseudostromquelle = None
        self.max_iterations_pseudostromquelle = None
        self.tolerance_pseudostromquelle = None
        self.max_voltage_pseudostromquelle = None
        self.delay_messung = None
        self.trennzeichen = None
        self.format_export = None
        self.window_height = None
        self.window_width = None

        # Lädt die Konfigurationswerte aus der Datei
        self.load_config()

    def load_config(self):
        config = configparser.ConfigParser()

        try:
            config.read(self.config_path)

            # Werte aus der Datei auslesen
            self.address_power_source = config.get("Devices", "address_power_source", fallback='ASRL6::INSTR')
            self.address_frequency_generator = config.get("Devices", "address_frequency_generator", fallback='ASRL3::INSTR')
            self.address_multimeter = config.get("Devices", "address_multimeter", fallback='ASRL5::INSTR')
            self.step_size_pseudostromquelle = config.getfloat("Pseudostromquelle", "step_size", fallback=0.05)
            self.max_iterations_pseudostromquelle = config.getint("Pseudostromquelle", "max_iterations", fallback=50)
            self.tolerance_pseudostromquelle = config.getfloat("Pseudostromquelle", "tolerance", fallback=0.001)
            self.max_voltage_pseudostromquelle = config.getfloat("Pseudostromquelle", "max_voltage", fallback=30)
            self.delay_messung = config.getfloat("Messung", "delay_messung", fallback=0.5)
            self.format_export = config.get("Export", "format", fallback="csv")
            self.trennzeichen = config.get("Export", "trennzeichen", fallback=";")
            self.window_height = config.getint("GUI", "window_height", fallback=550)
            self.window_width = config.getint("GUI", "window_width", fallback=1500)


        except Exception as e:
            print(f"Fehler beim Laden der Konfiguration: {e}")

    def __str__(self):
        return f"""
        Config:
        address_power_source = {self.address_power_source}
        address_frequency_generator = {self.address_frequency_generator}
        address_multimeter = {self.address_multimeter}
        step_size_pseudostromquelle = {self.step_size_pseudostromquelle}
        max_iterations_pseudostromquelle = {self.max_iterations_pseudostromquelle}
        tolerance_pseudostromquelle = {self.tolerance_pseudostromquelle}
        max_voltage_pseudostromquelle = {self.max_voltage_pseudostromquelle}
        delay_messung = {self.delay_messung}
        trennzeichen = {self.trennzeichen}
        format_export = {self.format_export}
        window_height = {self.window_height}
        window_width = {self.window_width}
        """


if __name__ == "__main__":
    # Konfiguration laden
    config = Config()

    # Geladene Werte anzeigen
    print(config)
