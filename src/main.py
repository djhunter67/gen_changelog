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

    def get_all_commit_msg(self):
        """Get all commit messages"""
        return subprocess.check_output(
            ['git', 'log', '--pretty=%B']
        ).strip()

    def get_msg_keywords(self):
        """Get the commit message keywords indicated by the end of a colon"""
        keys = self.get_all_commit_msg()
        keys = keys.split(b'\n')
        keys = [key.split(b':')[0].strip().decode('utf-8')
                for key in keys if b':' in key]

        return keys


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
        import re

        match = re.search(r'## \[(.+)\]', changelog)
        if match:
            return match.group(1)
        else:
            return None

    def get_next_version(self, GitData):
        """Get the next version"""
        keys = GitData.get_msg_keywords()

        match keys:
            case x if "feat" in x:
                return "MINOR"
            case x if "fix" in x:
                return "PATCH"
            case _:
                return "NO CHANGE"


def main():

    git_data = GitData()

    print(f"\n{F.GREEN}git_data{R}: {git_data.get_msg_keywords()}\n")

    print(f"{F.YELLOW}get next version{R}: {GenerateChangelog().get_next_version(git_data)}\n")


if '__main__' == __name__:
    main()
