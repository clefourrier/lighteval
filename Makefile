.PHONY: dist

dist: pypi-clean pypi-dist pypi-upload

pypi-clean:
	mkdir -p dist sdist eggs wheels
	[ -d dist ] && find dist -iname '*.egg' -exec mv {} eggs \; || true
	[ -d dist ] && find dist -iname '*.whl' -exec mv {} wheels \; || true
	[ -d dist ] && find dist -iname '*.tar.gz' -exec mv {} sdist \; || true
	rm -rf build dist *.egg-info

pypi-dist:
	pipenv run python setup.py sdist

pypi-upload:
	twine check dist/* || true
	twine upload dist/* -r pypi --skip-existing
	twine upload dist/* -r pypitest --skip-existing
