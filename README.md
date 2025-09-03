# az-automation-runbook-python-hello-world

#### PRE-REQUISITES

Install the required tools
```bash
❯ mise install
```

Confirm `uv` and `python3` are installed
```bash
❯ uv --version
uv 0.8.14 (af856fb88 2025-08-28)
❯ python3 -V
Python 3.8.20
```

#### (Optional) Create a virtual environment

```bash
❯ uv venv --seed venv
Using CPython 3.8.20
Creating virtual environment at: venv
Activate with: source venv/bin/activate
❯ source .venv/bin/activate
```

#### Create and Test a package
Create a package
```bash
❯ uv init --package hello-world
❯ cd hello-world
❯ uv lock
❯ python -m build
```

Test the Package
```bash
❯ pip3 install dist/hello_world-0.1.0-py3-none-any.whl
❯ hello-world
Hello from hello-world!
```

#### Mise: Build, Install, and Test

```bash
❯ mise run t
[clean] $ rm -rf ./dist
[clean] $ pip list | grep hello-world && pip uninstall -y hello-world || echo

[build] $ python -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - uv_build>=0.8.14,<0.9.0
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - uv_build>=0.8.14,<0.9.0
* Getting build dependencies for wheel...
* Building wheel...
Successfully built hello_world-0.1.0.tar.gz and hello_world-0.1.0-py3-none-any.whl

[install] $ pip install dist/hello_world-0.1.0-py3-none-any.whl
Processing ./dist/hello_world-0.1.0-py3-none-any.whl
Installing collected packages: hello-world
Successfully installed hello-world-0.1.0

[test] $ hello-world
Hello from hello-world!
Finished in 2.32s
```
