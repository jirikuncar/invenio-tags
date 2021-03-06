# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Tags bundles."""

from __future__ import unicode_literals

from invenio.base.bundles import styles as _css
from invenio.ext.assets import Bundle


_css.contents.append("css/tags/popover.css")

js = Bundle(
    "js/tags/record_editor.js",
    output="tags.js",
    weight=20,
    filters="uglifyjs"  # beautify couldn't do anything here ;-)
)
