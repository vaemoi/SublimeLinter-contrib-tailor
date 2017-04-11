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

    syntax = ''
    cmd = 'tailor'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.12.0'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

