

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import CountdownTracker

Rectangle {
    width: Constants.width
    height: Constants.height
    color: "#ffffff"
    border.color: "#ffffff"

    Text {
        id: text1
        x: 18
        y: 13
        width: 474
        height: 16
        text: qsTr("Music Show Tracking")
        font.pixelSize: 30
        font.bold: true
    }

    Image {
        id: image
        x: 18
        y: 63
        width: 100
        height: 100
        source: "qrc:/qtquickplugin/images/template_image.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: image1
        x: 18
        y: 187
        width: 100
        height: 100
        source: "qrc:/qtquickplugin/images/template_image.png"
        fillMode: Image.PreserveAspectFit
    }

    Label {
        id: seven_days_label
        x: 149
        y: 67
        width: 459
        height: 96
        color: "#000000"
        text: qsTr("dd:hh:mm:ss")
        font.family: "Courier"
        font.pointSize: 50
    }

    Text {
        id: text2
        x: 180
        y: 162
        width: 28
        height: 23
        text: qsTr("DAYS")
        font.pixelSize: 12
    }

    Text {
        id: text3
        x: 285
        y: 162
        width: 52
        height: 23
        text: qsTr("HOURS")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
    }

    Text {
        id: text4
        x: 405
        y: 162
        width: 52
        height: 23
        text: qsTr("MINUTES")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
    }

    Text {
        id: text5
        x: 522
        y: 162
        width: 52
        height: 23
        text: qsTr("SECONDS")
        font.pixelSize: 12
    }

    Label {
        id: eight_days_label
        x: 149
        y: 191
        width: 459
        height: 96
        color: "#000000"
        text: qsTr("dd:hh:mm:ss")
        font.family: "Courier"
        font.pointSize: 50
    }
}

/*##^##
Designer {
    D{i:0;height:300;width:650}
}
##^##*/
