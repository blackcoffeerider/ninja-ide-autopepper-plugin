# -*- coding: UTF-8 -*-
# autopepper.py
#
# Copyright (C) ninja-ide.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#  This plugins allows you to have your code pretty-printed
#   according to PEP8 by pressing CTRL+SHIFT+P.
#  It uses autopep8 as a library under the hood ;-)
#
# Initial development: blackcoffeerider
#  Version: 0.3
#  Known problems:
#   [ ] The history has a blank state in between the "meessy" and the "pretty"
#        version - this is due to the fact that there is no "instant"
#        replacement method for all the buffer contet of the QText Control :-(
#

# metadata
" AutoPepper "
__version__ = ' 0.3 '
__license__ = ' GPL '
__author__ = ' blackcoffeerider, Belug '
__email__ = ' blackcoffeerider@gmail.com, belug@gmail.com" '
__url__ = ''
__date__ = ' 08/06/2013 '
__prj__ = ' autopepper '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
import autopep8

from PyQt4.QtGui import QAction
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QObject
from PyQt4 import QtCore
from ninja_ide.core import plugin

# Plugin definition


class AutoPepper(plugin.Plugin):

    def initialize(self):
        # Init your plugin
        self.editor_s = self.locator.get_service('editor')
        self.menuApp_s = self.locator.get_service('menuApp')
        self.editor_s.editorKeyPressEvent.connect(self._handle_keypress)
        self._add_menu()

    def finish(self):
        # Shutdown your plugin
        pass

    def get_preferences_widget(self):
        # Return a widget for customize your plugin
        pass

    def _handle_keypress(self, event):

        keyMod = event.modifiers()

        is_SHIFT = keyMod & QtCore.Qt.ShiftModifier
        is_CTRL = keyMod & QtCore.Qt.ControlModifier

        is_shortcut = (is_SHIFT and is_CTRL and event.key() == QtCore.Qt.Key_P)
        if is_shortcut:
            self._rewrite_pep8()
        return

    def _open_with_pep8(self):
        editorWidget = self.editor_s.get_editor()
        if editorWidget:
            source = self.editor_s.get_text()
            fixed_source = autopep8.fix_string(source)
            self.editor_s.add_editor("", fixed_source, "py")

    def _rewrite_pep8(self):
        editorWidget = self.editor_s.get_editor()
        if editorWidget:
            source = self.editor_s.get_text()
            fixed_source = autopep8.fix_string(source)
            emi = Emitter(editorWidget)
            emi.emitClearToText()

            self.editor_s.insert_text(fixed_source)

    def _add_menu(self):
        autopep_action = QAction("Open with more Pep8", self)
        self.menuApp_s.add_action(autopep_action)
        self.connect(autopep_action,
                     SIGNAL("triggered()"),
                     self._open_with_pep8)


class Emitter (QObject):

    def __init__(self, textobj):
        QObject.__init__(self)
        self.textobj = textobj
        QObject.connect(self, SIGNAL("void_sellall()"), textobj.selectAll)
        QObject.connect(self, SIGNAL("void_cut()"), textobj.cut)

    def emitClearToText(self):
        self.emit(SIGNAL("void_sellall()"))
        self.emit(SIGNAL("void_cut()"))
