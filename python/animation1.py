from rich.console import Console
from rich.progress import Progress

console = Console()

with Progress() as progress:
    task_id = progress.add_task("[magenta]Spinning Pipe...", total=100)

    while True:
        for i in range(1, 101):
            progress.update(task_id, completed=i)
            progress.refresh()
            console.print("[green]|[/]" * (i % 4), end="\r")
            time.sleep(0.1)