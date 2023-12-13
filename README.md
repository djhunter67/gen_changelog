# Changelog Generator

## Usage

```bash
$ ./gen_changelog
```

## Synopsis
- The script will generate a changelog based on the git commit history.
- The version number is based on the initial git tag.
- The latest git tag will be generated and set.
- The changelog will be erased and regenerated every time the script is run.
- The changelog will be generated in the git root directory.
- The changelog will be generated in markdown format.

## Requirements
- git
- python3

## Installation
- pip install gen_changelog

## Changelog Format

```markdown
# CHANGELOG

Author: Hunter, Christerpher

All notable changes will be appended here.

This project, henceforth, will recongnize [semantic versioning](https://semver.org/).

## [⭐.✴️.✳️] - YEAR MONTH DAY

Here we write upgrade and change notes.

⭐ MAJOR version when you make incompatible API changes,

✴️ MINOR version when you add functionality in a backwards compatible manner

✳️ PATCH version when you make backwards compatible bug fixes.

--------------------------------------
```
