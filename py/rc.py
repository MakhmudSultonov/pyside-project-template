# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.9.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x8a\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Wi\
ndow\x0d\x0a\x0d\x0aWindow {\
\x0d\x0a    width: 640\
\x0d\x0a    height: 48\
0\x0d\x0a    visible: \
true\x0d\x0a    title:\
 qsTr(\x22Hello Wor\
ld\x22)\x0d\x0a}\x0d\x0a\
\x00\x00\x03\xd7\
#\
 This Python fil\
e uses the follo\
wing encoding: u\
tf-8\x0d\x0a\x0d\x0aimport s\
ys, os\x0d\x0a\x0d\x0afrom P\
ySide6.QtWidgets\
 import QApplica\
tion\x0d\x0afrom PySid\
e6.QtQml import \
QQmlApplicationE\
ngine, qmlRegist\
erSingletonType\x0d\
\x0afrom PySide6.Qt\
Core import QUrl\
, QCoreApplicati\
on\x0d\x0afrom PySide6\
.QtQuickControls\
2 import QQuickS\
tyle\x0d\x0a\x0d\x0aimport r\
c\x0d\x0aimport sys\x0d\x0af\
rom pathlib impo\
rt Path\x0d\x0a\x0d\x0afrom \
PySide6.QtGui im\
port QGuiApplica\
tion\x0d\x0afrom PySid\
e6.QtQml import \
QQmlApplicationE\
ngine\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0adef\
 main():\x0d\x0a    ap\
p = QApplication\
(sys.argv)\x0d\x0a\x0d\x0a  \
  QCoreApplicati\
on.setOrganizati\
onName(\x22Project\x22\
)\x0d\x0a    QCoreAppl\
ication.setOrgan\
izationDomain(\x22e\
xample\x22)\x0d\x0a    QC\
oreApplication.s\
etApplicationNam\
e(\x22example\x22)\x0d\x0a\x0d\x0a\
    QQuickStyle.\
setStyle(\x22Fusion\
\x22)\x0d\x0a    qmlRegis\
terSingletonType\
(QUrl(\x22qrc:/Them\
e.qml\x22), 'Theme'\
, 1, 0, 'Theme')\
\x0d\x0a\x0d\x0a    engine =\
 QQmlApplication\
Engine()\x0d\x0a    en\
gine.load(QUrl(\x22\
qrc:/qml/main.qm\
l\x22))\x0d\x0a\x0d\x0a    if n\
ot engine.rootOb\
jects():\x0d\x0a      \
  sys.exit(-1)\x0d\x0a\
\x0d\x0a    sys.exit(a\
pp.exec())\x0d\x0a\x0d\x0aif\
 __name__ == \x22__\
main__\x22:\x0d\x0a    ma\
in()\x0d\x0a\
"

qt_resource_name = b"\
\x00\x02\
\x00\x00\x07y\
\x00p\
\x00y\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x07\
\x03\x80\x15\x99\
\x00m\
\x00a\x00i\x00n\x00.\x00p\x00y\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0a\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x96\xc3\xd5\xb0\xdd\
\x00\x00\x00,\x00\x00\x00\x00\x00\x01\x00\x00\x00\x8e\
\x00\x00\x01\x96\xc4\x9f\xbc\x91\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
