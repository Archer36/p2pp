__author__ = 'Tom Van den Eede'
__copyright__ = 'Copyright 2018-2020, Palette2 Splicer Post Processing Project'
__credits__ = ['Tom Van den Eede',
               'Tim Brookman'
               ]
__license__ = 'GPLv3'
__maintainer__ = 'Tom Van den Eede'
__email__ = 'P2PP@pandora.be'
__status__ = 'BETA'


# general version info
MajorVersion = 6
MinorVersion = 2
Build = 1

releaseinfo = {
    '4.16.0': "final release for PrusaSlicer 2.2.0",
    '5.0.0': "Development start for PrusaSlicer 2.3.0",
    '5.1.0': "Automatic detection of bed origin and size",
    '5.2.0': "Static side purge",
    '5.2.1': "Extruder clear added on static purge",
    '5.3.0': "error in minimal linear ping length error string",
    '5.4.0': "corrected is_movement_command checking",
    '5.5.0': "correction in non-synched support material handling",
    '5.6.0': "updated in Aboslute conversion post processing",
    '5.7.0': "Fixup More than 4 color print",
    "5.10.0": "General code restructuring for optimized processing",
    "5.10.1": "further process optimization",
    "5.10.2": "typo correction in TOOLSTART processing",
    "5.11.0": "memory usage optimization",
    "5.12.0": "further memory usage optimization, speed optimization",
    "5.13.0": "weekend development cut off with some bugfixes",
    "5.14.0": "rewrite path processing routines",
    "5.15.0": "taken care to retain empty comments",
    "5.16.0": "fixup Z-move after unload",
    "5.17.0": "fixup error when doing unprocessed tower entry",
    "5.18.0": "MAF file is generated as BINARY file",
    "5.19.0": "update to config parsin from prusa settings instead of parsing in full file",
    "5.20.0": "updated parseline routine to prevent repetitive function call",
    "5.21.0": "small correction in gui and filemant type processing",
    "5.22.0": "corrected tower delta",
    "5.23.0": "better tower detection",
    "5.24.0": "DO_NOT_GENERATE_M0 option added",
    "5.25.0": "possible incorrect tool select - corrected",
    "5.26.0": "remove M0 from existing output",
    "5.27.0": "correction in the tower delta calculation",
    "6.0.0":  "Switched to Qt gui + corrected variable layer",
    "6.0.1":  "Corrected info to enter to make sure it works in PS2.2",
    "6.0.2":  "OMEGA Error generation caused exception",
    "6.0.3":  "Updated internal logo / some minor corrections",
    "6.0.4":  "general changes to what is error vs information",
    "6.1.0":  "correction for asynchronous call ion MACOS + exist statements ",
    "6.1.1":  "resizable form",
    "6.1.2":  "windows version update - added ! in the outut path so it can be copied directly",
    "6.1.3":  "correction empty grid after tool purge should not be dropped (sidewipe)",
    "6.1.4":  "added positioning speed correction after removing the unload code",
    "6.1.5":  "swapped z-height correction nin unprocessed code with movement command to avoid collisions",
    "6.1.6":  "Introduction of configurator using -config flag",
    "6.1.7":  "ICorrection full purge first tool change",
    "6.1.8":  "configuraton - added basic material support",
    "6.2.0":  "configuraton - basic support for default configs",
    "6.2.1":  "Pressure Advance processing M527 added - tool number gets reset to 0",
    '--- RELEASE INFORMATION': 'END'
}

latest_stable_version = ""

Version = "{}.{:02}.{:02}".format(MajorVersion, MinorVersion, Build)

if __name__ == "__main__":
    print(Version)
