#!/usr/bin/env python

"""
Generate the changelog for the current git environment
and write it to the file CHANGELOG.md
"""


import pathlib as path
import subprocess
import datetime
from colorama import Fore as F

R = F.RESET


def get_current_date():
    """Get the current date"""
    return datetime.datetime.now().strftime("%Y-%m-%d")


class GitData:
    """Class to hold git data"""

    def __str__(self):
        return "GitData: branch: %s, tag: %s, commit: %s" % (
            str(self.branch),
            str(self.tag),
            str(self.commit)
        )

    def get_current_branch(self):
        """Get the current git branch"""
        return subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
        ).strip()

    def get_current_tag(self):
        """Get the current git tag"""
        return subprocess.check_output(
            ['git', 'describe', '--abbrev=0', '--tags']
        ).strip()

    def get_current_commit(self):
        """Get the current git commit hash"""
        return subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']
        ).strip()

    def get_last_commit_msg(self):
        """Get the last commit message"""
        return subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B']
        ).strip()

    def get_msg_keywords(self):
        """Get the commit message keywords indicated by the end of a colon"""
        keys = self.get_last_commit_msg().split(b':')[0]

        return keys.decode('utf-8')


class ChangelogTemplate:

    def __repr__(self):
        return """
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

"""


class GenerateChangelog:

    def __init__(self):
        pass

    def get_changelog(self):
        """Look for the CHANGELOG.md file and return it's contents"""
        if path.exists('CHANGELOG.md'):
            with open('CHANGELOG.md', 'r') as file:
                return file.read()
        else:
            return None

    def write_changelog(self, changelog):

        with open('CHANGELOG.md', 'w') as file:
            file.write(changelog)

    def get_current_version(self, changelog):
        """Get the current version from the changelog"""
        match = re.search(r'## \[(\d+.\d+.\d+)\]', changelog)
        if match:
            return match.group(1)
        else:
            return None

    def get_next_version(self, current_version):
        """Get the next version"""
        if current_version:
            version = current_version.split('.')
            version[-1] = str(int(version[-1]) + 1)
            return '.'.join(version)
        else:
            return None


def main():

    git_data = GitData()

    print(f"\n{F.GREEN}git_data{R}: {git_data.get_msg_keywords()}\n")


if '__main__' == __name__:
    main()
