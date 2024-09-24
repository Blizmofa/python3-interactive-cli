from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich.json import JSON
from rich.text import Text
from rich.theme import Theme
from rich.progress import Progress
from rich.panel import Panel
from rich.console import Group
from PIL import Image


class RichDisplay:
    def __init__(self, theme: Theme = Theme({"primary": "cyan", "secondary": "magenta"})):
        self.console = Console(theme=theme)

    def display_table(self, data: list, title: str = None):
        """Display data in a formatted table."""
        table = Table(title=title or "Table")
        # Adding columns based on the keys of the first dictionary in the data list
        if data:
            headers = data[0].keys()
            for header in headers:
                table.add_column(header)
            # Adding rows
            for item in data:
                table.add_row(*(str(item[key]) for key in headers))
        self.console.print(table)

    def display_panel(self, content: str, title: str = None):
        """Display content in a panel."""
        panel = Panel(content, title=title or "Panel", border_style="green")
        self.console.print(panel)

    def display_markdown(self, markdown_content: str):
        """Display content in markdown format."""
        md = Markdown(markdown_content)
        self.console.print(md)

    def display_json(self, json_content: str):
        """Display JSON content in a formatted style."""
        json_data = JSON(json_content)
        self.console.print(json_data)

    def display_text(self, text: str, style: str = None):
        """Display styled text."""
        rich_text = Text(text, style=style or "white")
        self.console.print(rich_text)

    def display_ascii(self, ascii_art: str):
        """Display ASCII art."""
        self.console.print(ascii_art)

    def display_success(self, message: str):
        """Display a success message."""
        self.console.print(Text(message, style="bold green"))

    def display_warning(self, message: str):
        """Display a warning message."""
        self.console.print(Text(message, style="bold yellow"))

    def display_error(self, message: str):
        """Display an error message."""
        self.console.print(Text(message, style="bold red"))

    def display_progress(self, total: int):
        """Display a progress bar."""
        with Progress() as progress:
            task = progress.add_task("Processing...", total=total)
            while not progress.finished:
                progress.update(task, advance=1)

    def display_image(self, image_path: str):
        """Display an image (if supported by the console)."""

        try:
            image = Image.open(image_path)
            self.console.print(Panel(Group(image), title="Image"))
        except Exception as e:
            self.display_error(f"Could not display image: {e}")

