from rich_display.rich_output_manager import RichOutputManager

class CLI:
    def __init__(self):
        # Create an instance of the RichOutputManager
        self.rich_output_manager = RichOutputManager()

    def run(self):
        """Main method to run the CLI"""
        print("Starting CLI...")

        self.rich_output_manager.display_random_ascii()

        # Call the run method from RichOutputManager
        self.rich_output_manager.run()


if __name__ == "__main__":
    # Instantiate the CLI and run it
    cli = CLI()
    cli.run()
