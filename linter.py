#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by brwnrclse
# Copyright (c) 2017
#
# License: MIT
#

"""This module exports the Tailor plugin class."""

from SublimeLinter.lint import Linter, util


class Tailor(Linter):
    """Provides an interface to tailor."""

    cmd = 'tailor'
    config_file = ('-c', '.tailor.yml', '~')
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>error)|(?P<warning>warning)) '
        r'(?P<message>.+)'
    )
    multiline = False
    tempfile_suffix = 'swift'
    error_stream = util.STREAM_BOTH
    selectors = {}
    defaults = {
        'selector': 'source.swift',
        '--ignore=,': '',
        '--warn=,': '',
        '--error=,': ''
    }
