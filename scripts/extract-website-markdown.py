# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx",
#   "markdown",
#   "typer",
# ]
# ///

from pathlib import Path

import httpx  # noqa
import markdown
from typer import Typer, echo  # noqa

cli = Typer()


def ensure_path_has_extension(path: Path, desired_extension: str):
    """
    Ensures that the given Path object has the specified extension.

    If the path already has a different extension, it is replaced with the desired extension.
    The original filename without the extension is preserved.

    Args:
        path (pathlib.Path): The path object to check and modify if necessary.
        desired_extension (str): The desired extension for the path, including the dot (e.g., '.txt').

    Returns:
        pathlib.Path: The modified path with the desired extension.
    """
    # Extract the filename without the extension
    base_name = path.stem

    # Create a new path with the desired extension
    new_path = Path(f"{base_name}{desired_extension}")

    # Ensure the new path is in the same directory as the original path
    new_path = path.parent / new_path

    return new_path


@cli.command()
def save_website_as_markdown(url, output: Path):
    # Create an HTTP client
    http = httpx.Client()

    assert not output.exists() or output.is_file

    output = ensure_path_has_extension(output, ".md")

    # Fetch the content of the website
    response = http.get(url)

    if response.status_code == 200:
        # Extract the text content of the website
        content = response.text

        # Create a Markdown instance
        md = markdown.Markdown()

        # Convert HTML to Markdown
        markdown_content = md.convert(content)

        # Write the Markdown content to a file
        with open(output, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        echo(f"Website contents saved as {output}")
    else:
        echo(f"Failed to fetch the website. HTTP status code: {response.status_code}")


if __name__ == "__main__":
    cli()
