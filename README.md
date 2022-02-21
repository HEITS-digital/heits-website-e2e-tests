# heits-website-e2e-tests

CLI run commands :

Install all project dependencies using `pip install -r requirements.txt`

| `pytest --browser chromium` | run all the tests in headless mode with chrome \
| `pytest --browser chromium --html=report.html` | run all the tests in headless mode with chromium and generate standard pytest html report  \
| `pytest tests/test_home.py --browser chromium ` | run all the tests in headless mode from specified .py file
| `pytest` | run all the tests in headless mode \

Information regarding pytest html report [Pytest html report](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
Information regarding [CLI commands on playwright](https://playwright.dev/python/docs/test-runners/) e.g:

| arg names             | Description                           |
|------------------|---------------------------------------|
| `--browser` | specifies browser type e.g. chromium, firefox, webkit|
| `--slowmo` | runs the tests in slow motion e.g. --slowmo=500  |
| `--device` | runs the tests on specified device e.g. --device=iPhone 11  |
| `--headed` | runs the tests in the opened browser  |