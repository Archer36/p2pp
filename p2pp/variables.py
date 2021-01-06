
__author__ = 'Tom Van den Eede'
__copyright__ = 'Copyright 2018-2020, Palette2 Splicer Post Processing Project'
__credits__ = ['Tom Van den Eede',
               'Tim Brookman'
               ]
__license__ = 'GPLv3'
__maintainer__ = 'Tom Van den Eede'
__email__ = 'P2PP@pandora.be'

import re

#########################################
# Variable default values
#########################################

# Filament Transition Table
palette_inputs_used = [False,
                       False,
                       False,
                       False]

filament_type = [""] * 20

filament_color_code = ["-"] * 20

filament_short = [0, 0, 0, 0]

retraction = 0.0
retract_lift = [0.6, 0.6, 0.6, 0.6]
retract_length = [0.8, 0.8, 0.8, 0.8]
filament_diameter = [1.75, 1.75, 1.75, 1.75]
filament_ids = []
nozzle_diameter = 0.4

wiping_info = []
accessory_mode = False  # type Bool


palette_plus = False
palette_plus_loading_offset = -9
palette_plus_ppm = -9

skippable_layer = []  # type array of bool

used_filament_types = []  # type array of string

default_splice_algorithm = "D000 D000 D000"  # type string
process_warnings = []  # type array of string
splice_algorithm_table = []  # type array of string
splice_algorithm_dictionary = {}  # type dictionary Str->Str

tower_delta = False
max_tower_z_delta = 0.0  # type float
cur_tower_z_delta = 0.0  # type float
layer_height = 0.2  # type float
first_layer_height = 0.2  # type float
towerskipped = False  # type bool

printer_profile_string = ''
default_printerprofile = '50325050494e464f'
# A unique ID linked to a printer configuration profile in the Palette 2 hardware.

input_gcode = []
processed_gcode = []  # final output array with Gcode

# These variables are used to build the splice information table (Omega-30 commands in GCode) that drives the Palette2.
# spliceoffset allows for a correction of the position at which the transition occurs.
# When the first transition is scheduled to occur at 120mm in GCode, you can add a number of mm to push the transition
# further in the purge tower.  This serves a similar function as the transition offset in chroma.
splice_offset = 0  # type: int
splice_extruder_position = []
splice_used_tool = []
splice_length = []

# SIDE WIPES
side_wipe_loc = ""  # type: str
side_wipe = False  # type: bool
side_wipe_length = 0  # type: float
sidewipe_miny = 25  # type: float
sidewipe_maxy = 175  # type: float
wipe_feedrate = 3000  # type: int
toolchange_start = False
toolchange_processed = False
enterpurge = False
variable_layer = False
save_unprocessed = False

purge_keep_x = None
purge_keep_y = None
previous_purge_keep_x = None
previous_purge_keep_y = None
needpurgetower = False

before_sidewipe_gcode = []
after_sidewipe_gcode = []

filename = ""

bed_size_x = -9999  # type: float
bed_size_y = -9999  # type: float
bed_origin_x = -9999  # type: float
bed_origin_y = -9999  # type: float  # Account for the purge line at the start of the print
bed_max_x = -9999 # type: float
bed_max_y = -9999 # type: float
bed_shape_warning = False
bed_shape_rect = True

# wipe_feedrates = {}

wipe_tower_info_minx = 9999
wipe_tower_info_miny = 9999
wipe_tower_info_maxx = -9999
wipe_tower_info_maxy = -9999
wipe_tower_xsize = 0
wipe_tower_ysize = 0


wipetower_posx = 0.0  # type: float
wipetower_posy = 0.0  # type: float
wipetower_width = 0.0  # type: float
extrusion_width = 0.45  # type: float

current_position_x = 0.0  # type: float
current_position_y = 0.0  # type: float
current_position_z = 0.0  # type: float

previous_position_x = 0.0
previous_position_y = 0.0

# ping_extruder_position: Stores information about the PINGS generated by P2PP. This information is pasted after
# the splice information directly below the Palette2 header in GCODE.
ping_extruder_position = []
ping_extrusion_between_pause = []

# hotswapcount: The number of hot-swaps generated during the print. This feature is currently unused.
hotswap_count = 0  # type: int

# TotalExtrusion keeps track of the total extrusion in mm for the print taking into account the Extruder Multiplier set
# in the GCode settings...
total_material_extruded = 0  # type: float
material_extruded_per_color = [0, 0, 0, 0]
last_ping_extruder_position = 0
ping_interval = 350  # type: float
max_ping_interval = 3000  # type: float
ping_length_multiplier = 1.03  # type: float
sidewipe_correction = 1.0  # type: float
autoaddsplice = False  # type: bool
autoadded_purge = 0.0  # type: float

absolute_extruder = False  # type : bool

previous_tool = -1
current_tool = -1  # type: int
set_tool = -1  # type: int
previous_toolchange_location = 0  # type: float

current_layer = "0"  # type: str # Capture layer information for short splice texts

extrusion_multiplier = 1.0  # type: float  # Monitors M221 commands during the print.
current_print_feedrate = 100  # type: int  # Monitors the current feedrate
current_print_feed = 2000  # type: int
extra_runout_filament = 150  # type: int  # Provide extra filament at the end of the print.
min_splice_length = 70  # type: int  # Minimum overall splice length.
min_start_splice_length = 100  # type: int  # Minimum first splice length.

consolewait = False

version = "0.0.0"
processtime = 0

versioncheck = False
upgradeprocess = None

full_purge_reduction = False
purge_first_empty = True
purgelayer = 0

parsed_gcode = []
_obsolete_gcodeclass = []
_obsolete_linetool = []
_obsolete_parsecomment = []
_obsolete_layernumber = []
lasthopup = 0
create_tower_entry = False
acc_ping_left = 0.0
infill_speed = 0.0
keep_hopspec = 0
keep_hopcorrection = 0
last_parsed_layer = -1
current_layer_is_skippable = False

process_temp = False
current_temp = 0
new_temp = 0
temp1_stored_command = ""
temp2_stored_command = ""
tx_offset = 0   #offset for temp wait positions
ty_offset = 0
block_classification = 0
previous_block_classification = 0
powerchaos = False
retract_move = False
max_tower_delta = 0.0
min_tower_delta = 0.0

retract_x = None
retract_y = None

purge_pos_x = 0
purge_pos_y = 0

saved_fanspeed = 0
ignore_warnings = False

purge_sequence_x = 0
purge_sequence_y = 0

backpassed = False
post_tower = False

# prusa side wipe contraption
bigbrain3d_x_position = 256.5
bigbrain3d_y_position = None
bigbrain3d_blob_cooling_time = 12
bigbrain3d_blob_size = 40
bigbrain3d_blob_speed = 200
bigbrain3d_purge_enabled = False
bigbrain3d_smartfan = False
bigbrain3d_motorpower_high = 450
bigbrain3d_motorpower_normal = 300
bigbrain3d_whacks = 1
bigbrain3d_fanoffdelay = 0
bigbrain3d_left = 1
bigbrain3d_prime = 0

tower_measure = False
expect_retract = False

keep_speed = 0

purgetopspeed = 99999
wipe_remove_sparse_layers = False

ps_version = "No version info detected"

debug_leaveToolCommands = False

synced_support = True
support_material = False

skirtsize = 0
skirts = 0

autoloadingoffset = 0

classes = {
    0: "Undefined     ",
    1: "Normal GCode  ",
    2: "TChange START ",
    4: "TCHange UNLOAD",
    8: "TChange PURGE ",
    16: "Empty Grid    ",
    32: "BRIM          ",
    64: "BRIM END      ",
    128: "END GRID      ",
    256: "COMMENT ONLY  ",
    512: "END PURGE     ",
    1024: "TOOL COMMAND  ",
    2048: "RETURN TO NORM"

}


# more than 4 color prints

m4c_enabled = False
m4c_toolchanges = []
m4c_toolchange_source_positions = []
m4c_loadedinputs = []
m4c_early_tool = []
m4c_early_warning = []
m4c_late_warning = []
m4c_color_table = []
m4c_numberoffilaments = 4


m4c_headerinfo = []

regex_p2pp = re.compile("^;\s*P2PP\s+([^=]+)=?(.*)$")

# conversion to absolute extruder:

absolute_counter = -9999
layer_end = []
last_layer_processed = -1

layer_toolchange_counter = 0
layer_emptygrid_counter = 0

generate_M0 = True

exit_enabled = False

side_wipe_state = 0

filament_count = 4

# manual swap
manual_filament_swap = False
z_maxheight = -1

# bed projection
bed = None
bedtrace = False


#klipper support
klipper = False


# disabke Z-movements during low tower

disable_z = False