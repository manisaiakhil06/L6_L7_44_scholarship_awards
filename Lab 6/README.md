# Lab 6 — Code and Branch Coverage

The scholarship award module is tested with pytest and coverage.py.

## Run

From this directory:

```bash
python -m pip install pytest coverage
python -m pytest -q
python -m coverage run --source=scholarship_awards -m pytest -q
python -m coverage report -m
python -m coverage erase
python -m coverage run --branch --source=scholarship_awards -m pytest -q
python -m coverage report -m
```

`CodeCoverageTest_44_application.py` focuses on statement execution; `BranchCoverageTest_44_application.py` explicitly exercises true and false outcomes. `test_scholarship_awards.py` contains the full regression suite. Capture the final terminal output after running the commands locally for the lab screenshots.
