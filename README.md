# heits-website-e2e-tests

CLI run commands :

| `pytest` | run all the tests in headless mode \
| `pytest tests/test_home.py ` | run all the tests in headless mode from specified .py file

Information regarding [CLI commands on playwright](https://playwright.dev/python/docs/test-runners/) e.g:

| arg names             | Description                           |
|------------------|---------------------------------------|
| `--browser` | specifies browser type e.g. chrome, chromium, firefox|
| `--slowmo` | runs the tests in slow motion e.g. --slowmo=500  |
| `--device` | runs the tests on specified device e.g. --device=iPhone 11  |