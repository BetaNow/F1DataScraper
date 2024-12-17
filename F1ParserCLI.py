import sys
import yaml
from pathlib import Path
from rich.console import Console
from rich.panel import Panel


class F1ParserCLI:
    def __init__(self):
        self.console = Console()
        self.config = self.load_config()

    def load_config(self) -> dict:
        """
        Load configuration from config.json

        :return: Configuration
        """
        config_path = Path("config/config.yml")

        try:
            with open(config_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            self.console.print("[red]Error: config.yml not found in config directory[/red]")
            sys.exit(1)

    def run(self) -> None:
        """
        Main execution flow

        :return: None
        """
        self.console.print(Panel.fit("Welcome to F1 Data Parser!", title="Welcome", border_style="green"))


if __name__ == "__main__":
    cli = F1ParserCLI()
    cli.run()
