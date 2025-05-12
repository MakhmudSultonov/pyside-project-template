# This Python file uses the following encoding: utf-8

import sys, os

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonType
from PySide6.QtCore import QUrl, QCoreApplication
from PySide6.QtQuickControls2 import QQuickStyle

import rc

def main():
    app = QApplication(sys.argv)

    QCoreApplication.setOrganizationName("OrganizationName") #change to your organization name
    QCoreApplication.setOrganizationDomain("OrganizationDomain") #change to your organization domain
    QCoreApplication.setApplicationName("ApplicationName") #change to your application name

    QQuickStyle.setStyle("Fusion")
    qmlRegisterSingletonType(QUrl("qrc:/Theme.qml"), 'Theme', 1, 0, 'Theme')

    engine = QQmlApplicationEngine()
    engine.load(QUrl("qrc:/qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
