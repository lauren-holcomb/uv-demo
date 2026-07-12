# uv-demo

A small repo for practicing `uv`, project environments, and dependency
troubleshooting.

The point is not the Python code itself. The point is to see how a project
records the packages it needs, how `uv` uses those records, and what to do when
a script asks for a package that is not available in the current project
environment.

## Demo flow

After cloning the repo:

```bash
uv run python hello.py
```

This should run without needing any extra packages. The first time you run a
`uv` command in a project, you may see output about creating or updating the
project environment.

Next, look at `pyproject.toml`. Notice that this project already lists
`pandas` as a dependency.

Then try:

```bash
uv run python orders_summary.py
```

The script should get past `pandas`, but hit a `ModuleNotFoundError` for
`seaborn`.

Look at `pyproject.toml`, then add the missing dependency:

```bash
uv add seaborn
```

Look at `pyproject.toml` and `uv.lock` again, then rerun:

```bash
uv run python orders_summary.py
```

## What to notice

- `pyproject.toml` records project dependencies.
- `uv.lock` records exact resolved package versions after syncing or adding.
- `.venv/` is the local project environment.
- Git should track scripts, data, and dependency metadata.
- Git should not track `.venv/`.
