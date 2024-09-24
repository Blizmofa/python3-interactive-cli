from random import choice
from rich_display.rich_display import RichDisplay
from rich_display.ascii_patterns_manager import AsciiPatternsManager


class RichOutputManager:
    def __init__(self):
        self.rich_display = RichDisplay()

    def run(self):
        """Executes the display functionalities"""
        # Example data for table
        data = [
            {"ID": "1", "Name": "Alice", "Age": "24"},
            {"ID": "2", "Name": "Bob", "Age": "30"},
            {"ID": "3", "Name": "Charlie", "Age": "29"},
        ]

        # Display a table
        self.rich_display.display_table(data, title="User Info Table")

        # Display a panel with custom content
        self.rich_display.display_panel("This is a panel with custom content.", title="Custom Panel")

        # Display some markdown content
        markdown_content = """
        # Heading 1
        This is some **bold** text and *italic* text.

        ## Heading 2
        - Item 1
        - Item 2
        """
        self.rich_display.display_markdown(markdown_content)

        # Display styled text
        self.rich_display.display_text("Hello, World!", style="bold red")

        # Display JSON-like content
        json_content = '{"ID": 1, "Name": "Alice", "Age": 24}'
        self.rich_display.display_json(json_content)

        # Display success message
        self.rich_display.display_success("Data processed successfully!")

        # Display warning message
        self.rich_display.display_warning("This is a warning message.")

        # Display error message
        self.rich_display.display_error("This is an error message.")

        # Display a progress bar
        self.rich_display.display_progress(total=10)

        # Optionally, display an image (uncomment the line below if you have an image path)
        # self.rich_display.display_image("path_to_your_image.jpg")

    def display_random_ascii(self):
        """Displays a random ASCII pattern from both templates and files"""
        patterns = AsciiPatternsManager.get_all_patterns()  # Get all patterns
        if patterns:  # Check if there are patterns to choose from
            random_pattern = choice(patterns)
            self.rich_display.display_ascii(random_pattern)

