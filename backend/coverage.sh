# Run coverage and generate HTML report
coverage run --omit "./.venv/*" manage.py test -v 2

coverage html
