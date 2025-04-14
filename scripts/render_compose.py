#!uv run
# /// script
# dependencies = [
#   "jinja2",
#   "typer",
# ]
# ///

import os, enum
from typing import Optional
import typer
import jinja2
from pathlib import Path

env = jinja2.Environment()
cli = typer.Typer()


class Mode(str, enum.Enum):
    cpu = "cpu"
    cuda = "cuda"
    rocm = "rocm"


def build(
    mode: Mode = Mode.cpu,
    output: Optional[Path] = None,
    template_path: Path = Path("docker/_template.j2.yaml"),
):
    assert template_path.is_file()

    if output is None:
        output = template_path.parent / f"compose.{mode.value}.yaml"

    with open(template_path, "rt") as fp:
        template = env.from_string(fp.read())

    content = template.render(mode=mode)

    with open(output, "wt") as fp:
        fp.write(content)


typer.run(build)
