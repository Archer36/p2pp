__author__ = 'Tom Van den Eede'
__copyright__ = 'Copyright 2018-2020, Palette2 Splicer Post Processing Project'
__credits__ = ['Tom Van den Eede',
               'Tim Brookman'
               ]
__license__ = 'GPLv3'
__maintainer__ = 'Tom Van den Eede'
__email__ = 'P2PP@pandora.be'

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
import image_rc
import p2pp.variables as v
import p2pp.colornames as colornames
import version
import sys

last_pct = -10


def print_summary(summary):
    create_logitem("")
    create_logitem("-" * 19, "blue")
    create_logitem("   Print Summary", "blue")
    create_logitem("-" * 19, "blue")
    create_emptyline()
    create_logitem("Number of splices:    {0:5}".format(len(v.splice_extruder_position)))
    create_logitem("Number of pings:      {0:5}".format(len(v.ping_extruder_position)))
    create_logitem("Total print length {:-8.2f}mm".format(v.total_material_extruded))
    create_emptyline()
    if v.full_purge_reduction or v.tower_delta:
        create_logitem("Tower Delta Range  {:.2f}mm -  {:.2f}mm".format(v.min_tower_delta, v.max_tower_delta))
    create_emptyline()

    if v.m4c_numberoffilaments <= 4:
        create_logitem("-" * 22, "blue")
        create_logitem("Inputs/Materials used:", "blue")
        create_logitem("-" * 22, "blue")

        for i in range(len(v.palette_inputs_used)):
            if v.palette_inputs_used[i]:
                create_colordefinition(0, i + 1, v.filament_type[i], v.filament_color_code[i],
                                       v.material_extruded_per_color[i])

    else:
        create_logitem("-" * 14, "blue")
        create_logitem("Materials used:")
        create_logitem("-" * 14, "blue")
        for i in range(v.m4c_numberoffilaments):
            create_colordefinition(1, i + 1, v.filament_type[0], v.filament_color_code[i], 0)

        create_emptyline()
        create_logitem("-" * 27, "blue")
        create_logitem("Required Toolchanges: {}".format(len(v.m4c_headerinfo)))
        create_logitem("-" * 27, "blue")
        for i in v.m4c_headerinfo:
            create_logitem("      " + i)

    create_emptyline()
    for line in summary:
        create_logitem(line[1:].strip(), "black", False)
    create_emptyline()


def progress_string(pct):
    global last_pct
    if pct - last_pct < 2:
        return
    if int(last_pct/10) != int(pct/10):
        app.sync()

    form.progress.setProperty("value", min(100, pct))
    if pct >= 100:
        form.label_5.setText("")
        if len(v.process_warnings) == 0:
            form.textBrowser.setStyleSheet("background-color: #DDFFDD;")
            form.label_6.setText("COMPLETED OK")
            form.label_6.setStyleSheet("color: #008000")
        else:
            form.textBrowser.setStyleSheet("background-color: #FFDDDD;")
            form.label_6.setText("COMPLETED WITH WARNINGS")
            form.label_6.setStyleSheet("color: #FF0000")

    last_pct = pct



def create_logitem(text, color="#000000", force_update=True, position=0):
    word = '<span style=\" color: {}\">  {}</span>'.format(color, text)
    form.textBrowser.append( word )



def create_colordefinition(reporttype, p2_input, filament_type, color_code, filamentused):

    name = "----"
    if reporttype == 0:
        name = "Input"
    if reporttype == 1:
        name = "Filament"

    try:
        filament_id = v.filament_ids[p2_input - 1]
    except IndexError:
        filament_id = ""

    word = ''
    if reporttype == 0:
        word = "  \t{}  {} {:-8.2f}mm - {} <span style=\" color: #{};\">[######]]</span>   \t{:15} {} ".format(name, p2_input, filamentused, filament_type, color_code, colornames.find_nearest_colour(color_code), filament_id )

    if reporttype == 1:
        word = "  \t{}  {}  - {} <span style=\" color: #{};\">[######]]</span>   \t{:15} {}".format(name, p2_input, filament_type, color_code, colornames.find_nearest_colour(color_code), filament_id)

    form.textBrowser.append(word)

def create_emptyline():
    create_logitem('')


def on_click():
    app.exit(0)


def close_button_enable():
    if not v.exit_enabled:
        form.exitButton.clicked.connect(on_click)
        form.exitButton.setEnabled(True)
        v.exit_enabled = True
        app.exec_()


def setfilename(text):
    form.filename.setText(text)
    if text == "":
        form.filename.setText('')
        form.label_4.setText('')


def log_warning(text):
    v.process_warnings.append(";" + text)
    create_logitem(text, "#FF0000")


Form, Window = uic.loadUiType("p2pp.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
create_logitem("P2PP Version: {}".format(version.Version))
create_logitem("Python Version: {}".format(sys.version.split(' ')[0]))

if sys.platform != "Darwin":
    form.filename.setFont(QFont("Courier", 8))
    form.label_6.setFont(QFont("Courier", 10))
    form.label_5.setFont(QFont("Courier", 8))
    form.label_4.setFont(QFont("Courier", 8))
    form.label.setFont(QFont("Courier", 8))
    form.exitButton.setFont(QFont("Courier", 8))
    form.textBrowser.setFont(QFont("Courier", 8))

window.show()
app.sync()