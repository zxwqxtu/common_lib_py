# Example Package

This is a simple example package.

# 打包到pypi.org
[学习教程](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

# github markdown
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)

# 学习步骤
## Generating distribution archives
1. python3 -m pip install --upgrade build
2. python3 -m build

## Uploading distribution files to PyPI
1. python3 -m pip install --upgrade twine
2. python3 -m twine upload --repository testpypi dist/*
