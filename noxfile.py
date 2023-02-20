"""
Build and preview this theme documentation locally.

To build with a live-server:

    nox -s docs -- live

To re-install dependencies:

    nox -s docs -- -r
"""
import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session
def docs(session):
    session.install("-r", "docs/requirements.txt")
    build_command = ["-b", "html", "docs", "docs/_build/html"]
    if "live" in session.posargs:
        session.install("-e", ".[dev]")
        session.run("stb", "serve", "docs")
    else:
        session.install(".[dev]")
        session.run("stb", "compile")
        build_command = session.posargs + build_command
        session.run("sphinx-build", *build_command)
