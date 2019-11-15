# Moons of Jupyter

Run a single Jupyter Lab instance, connected to multiple Python environments.

⚠ **This is 100% vaporware. It's something I wish existed. Maybe I'll build it some day... want to help?** ⚠

```bash
$ pipx install moons-of-jupyter

$ moj start
Jupyter Lab running on http://localhost:9876/

$ moj add path/to/venv --name "Venv Project"
installing path/to/venv (venv environment, Python 3.7)... done

$ moj add path/to/poetry-project --name "Poetry Project"
installing path/to/poetry-project (Poetry environment, Python 3.5)... done

$ moj add path/to/pipenv-project --pythonpath
installing path/to/pipenv-project (Pipenv environment, Python 2.7)... done

$ moj add /usr/local/bin/python3
installing /usr/local/bin/python3 (base install, Python 3.8)... done

$ moj remove "Poetry Project"
removed path/to/poetry-project

$ moj remove /usr/local/bin/python3
removed /usr/local/bin/python3

$ moj autostart on
installed launchd config
moj will now run automatically on startup

$ moj autostart off
moj will no longer run on startup

```


