import os
import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from functools import partial
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.OpenMaya as OpenMaya

import pymel.core as pm

from common.utils import *
from common.Prefs import *


# ######################################################################################################################

_FILE_NAME_PREFS = "renderer_diagnosis"

# ######################################################################################################################


class RendererDiagnosis(QDialog):

    def __init__(self, prnt=wrapInstance(int(omui.MQtUtil.mainWindow()), QWidget)):
        super(RendererDiagnosis, self).__init__(prnt)
        
        # Common Preferences (common preferences on all tools)
        self.__common_prefs = Prefs()
        # Preferences for this tool
        self.__prefs = Prefs(_FILE_NAME_PREFS)

        # Model attributes

        # UI attributes
        self.__ui_width = 500
        self.__ui_height = 300
        self.__ui_min_width = 300
        self.__ui_min_height = 200
        self.__ui_pos = QDesktopWidget().availableGeometry().center() - QPoint(self.__ui_width, self.__ui_height)/2

        self.__retrieve_prefs()

        # name the window
        self.setWindowTitle("Renderer Diagnosis")
        # make the window a "tool" in Maya's eyes so that it stays on top when you click off
        self.setWindowFlags(QtCore.Qt.Tool)
        # Makes the object get deleted from memory, not just hidden, when it is closed.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Create the layout, linking it to actions and refresh the display
        self.__create_ui()
        self.__refresh_ui()

    def __save_prefs(self):
        """
        Save preferences
        :return:
        """
        size = self.size()
        self.__prefs["window_size"] = {"width": size.width(), "height": size.height()}
        pos = self.pos()
        self.__prefs["window_pos"] = {"x": pos.x(), "y": pos.y()}

    def __retrieve_prefs(self):
        """
        Retrieve preferences
        :return:
        """
        if "window_size" in self.__prefs:
            size = self.__prefs["window_size"]
            self.__ui_width = size["width"]
            self.__ui_height = size["height"]

        if "window_pos" in self.__prefs:
            pos = self.__prefs["window_pos"]
            self.__ui_pos = QPoint(pos["x"], pos["y"])

    def showEvent(self, arg__1: QShowEvent) -> None:
        """
        Add callbacks
        :return:
        """
        pass
        # self.__selection_callback = \
        #     OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.on_selection_changed)

    def hideEvent(self, arg__1: QCloseEvent) -> None:
        """
        Remove callbacks
        :return:
        """
        # OpenMaya.MMessage.removeCallback(self.__selection_callback)
        self.__save_prefs()

    def __create_ui(self):
        """
        Create the ui
        :return:
        """
        # Reinit attributes of the UI
        self.setMinimumSize(self.__ui_min_width, self.__ui_min_height)
        self.resize(self.__ui_width, self.__ui_height)
        self.move(self.__ui_pos)

        # asset_path = os.path.dirname(__file__) + "/assets/asset.png"

        # Main Layout
        main_lyt = QVBoxLayout()
        main_lyt.setContentsMargins(10, 15, 10, 15)
        main_lyt.setSpacing(12)
        self.setLayout(main_lyt)

    def __refresh_ui(self):
        """
        Refresh the ui according to the model attribute
        :return:
        """
        # TODO refresh the UI according to model attributes
        pass