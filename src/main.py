#!/usr/bin/env python

"""
Generate the changelog for the current git environment
and write it to the file CHANGELOG.md
"""


import os
import sys
import subprocess
import re
import datetime
import argparse


def get_current_branch():
    """Get the current git branch"""


def get_current_date():
    """Get the current date"""
    return datetime.datetime.now().strftime("%Y-%m-%d")


class GitData:
    """Class to hold git data"""

    def __str__(self):
        return "GitData: branch: %s, tag: %s, commit: %s" % (
            self.branch,
            self.tag,
            self.commit
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
