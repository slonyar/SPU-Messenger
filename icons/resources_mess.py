# file that connecting messenger gui with icons

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xf3\
\x3c\
\x73\x76\x67\x20\x78\x6d\x6c\x6e\x73\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x32\
\x34\x22\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x2d\x39\
\x36\x30\x20\x39\x36\x30\x20\x39\x36\x30\x22\x20\x77\x69\x64\x74\
\x68\x3d\x22\x32\x34\x22\x3e\x3c\x70\x61\x74\x68\x20\x64\x3d\x22\
\x4d\x32\x34\x30\x2d\x34\x30\x30\x68\x31\x32\x32\x6c\x32\x30\x30\
\x2d\x32\x30\x30\x71\x39\x2d\x39\x20\x31\x33\x2e\x35\x2d\x32\x30\
\x2e\x35\x54\x35\x38\x30\x2d\x36\x34\x33\x71\x30\x2d\x31\x31\x2d\
\x35\x2d\x32\x31\x2e\x35\x54\x35\x36\x32\x2d\x36\x38\x34\x6c\x2d\
\x33\x36\x2d\x33\x38\x71\x2d\x39\x2d\x39\x2d\x32\x30\x2d\x31\x33\
\x2e\x35\x74\x2d\x32\x33\x2d\x34\x2e\x35\x71\x2d\x31\x31\x20\x30\
\x2d\x32\x32\x2e\x35\x20\x34\x2e\x35\x54\x34\x34\x30\x2d\x37\x32\
\x32\x4c\x32\x34\x30\x2d\x35\x32\x32\x76\x31\x32\x32\x5a\x6d\x32\
\x38\x30\x2d\x32\x34\x33\x2d\x33\x37\x2d\x33\x37\x20\x33\x37\x20\
\x33\x37\x5a\x4d\x33\x30\x30\x2d\x34\x36\x30\x76\x2d\x33\x38\x6c\
\x31\x30\x31\x2d\x31\x30\x31\x20\x32\x30\x20\x31\x38\x20\x31\x38\
\x20\x32\x30\x2d\x31\x30\x31\x20\x31\x30\x31\x68\x2d\x33\x38\x5a\
\x6d\x31\x32\x31\x2d\x31\x32\x31\x20\x31\x38\x20\x32\x30\x2d\x33\
\x38\x2d\x33\x38\x20\x32\x30\x20\x31\x38\x5a\x6d\x32\x36\x20\x31\
\x38\x31\x68\x32\x37\x33\x76\x2d\x38\x30\x48\x35\x32\x37\x6c\x2d\
\x38\x30\x20\x38\x30\x5a\x4d\x38\x30\x2d\x38\x30\x76\x2d\x37\x32\
\x30\x71\x30\x2d\x33\x33\x20\x32\x33\x2e\x35\x2d\x35\x36\x2e\x35\
\x54\x31\x36\x30\x2d\x38\x38\x30\x68\x36\x34\x30\x71\x33\x33\x20\
\x30\x20\x35\x36\x2e\x35\x20\x32\x33\x2e\x35\x54\x38\x38\x30\x2d\
\x38\x30\x30\x76\x34\x38\x30\x71\x30\x20\x33\x33\x2d\x32\x33\x2e\
\x35\x20\x35\x36\x2e\x35\x54\x38\x30\x30\x2d\x32\x34\x30\x48\x32\
\x34\x30\x4c\x38\x30\x2d\x38\x30\x5a\x6d\x31\x32\x36\x2d\x32\x34\
\x30\x68\x35\x39\x34\x76\x2d\x34\x38\x30\x48\x31\x36\x30\x76\x35\
\x32\x35\x6c\x34\x36\x2d\x34\x35\x5a\x6d\x2d\x34\x36\x20\x30\x76\
\x2d\x34\x38\x30\x20\x34\x38\x30\x5a\x22\x2f\x3e\x3c\x2f\x73\x76\
\x67\x3e\
\x00\x00\x01\x02\
\x3c\
\x73\x76\x67\x20\x78\x6d\x6c\x6e\x73\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x32\
\x34\x22\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x2d\x39\
\x36\x30\x20\x39\x36\x30\x20\x39\x36\x30\x22\x20\x77\x69\x64\x74\
\x68\x3d\x22\x32\x34\x22\x3e\x3c\x70\x61\x74\x68\x20\x64\x3d\x22\
\x4d\x32\x30\x30\x2d\x31\x32\x30\x71\x2d\x33\x33\x20\x30\x2d\x35\
\x36\x2e\x35\x2d\x32\x33\x2e\x35\x54\x31\x32\x30\x2d\x32\x30\x30\
\x76\x2d\x35\x36\x30\x71\x30\x2d\x33\x33\x20\x32\x33\x2e\x35\x2d\
\x35\x36\x2e\x35\x54\x32\x30\x30\x2d\x38\x34\x30\x68\x32\x38\x30\
\x76\x38\x30\x48\x32\x30\x30\x76\x35\x36\x30\x68\x32\x38\x30\x76\
\x38\x30\x48\x32\x30\x30\x5a\x6d\x34\x34\x30\x2d\x31\x36\x30\x2d\
\x35\x35\x2d\x35\x38\x20\x31\x30\x32\x2d\x31\x30\x32\x48\x33\x36\
\x30\x76\x2d\x38\x30\x68\x33\x32\x37\x4c\x35\x38\x35\x2d\x36\x32\
\x32\x6c\x35\x35\x2d\x35\x38\x20\x32\x30\x30\x20\x32\x30\x30\x2d\
\x32\x30\x30\x20\x32\x30\x30\x5a\x22\x2f\x3e\x3c\x2f\x73\x76\x67\
\x3e\
\x00\x00\x02\x11\
\x3c\
\x73\x76\x67\x20\x78\x6d\x6c\x6e\x73\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x32\
\x34\x22\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x2d\x39\
\x36\x30\x20\x39\x36\x30\x20\x39\x36\x30\x22\x20\x77\x69\x64\x74\
\x68\x3d\x22\x32\x34\x22\x3e\x3c\x70\x61\x74\x68\x20\x64\x3d\x22\
\x4d\x34\x38\x30\x2d\x34\x38\x30\x71\x2d\x36\x36\x20\x30\x2d\x31\
\x31\x33\x2d\x34\x37\x74\x2d\x34\x37\x2d\x31\x31\x33\x71\x30\x2d\
\x36\x36\x20\x34\x37\x2d\x31\x31\x33\x74\x31\x31\x33\x2d\x34\x37\
\x71\x36\x36\x20\x30\x20\x31\x31\x33\x20\x34\x37\x74\x34\x37\x20\
\x31\x31\x33\x71\x30\x20\x36\x36\x2d\x34\x37\x20\x31\x31\x33\x74\
\x2d\x31\x31\x33\x20\x34\x37\x5a\x4d\x31\x36\x30\x2d\x31\x36\x30\
\x76\x2d\x31\x31\x32\x71\x30\x2d\x33\x34\x20\x31\x37\x2e\x35\x2d\
\x36\x32\x2e\x35\x54\x32\x32\x34\x2d\x33\x37\x38\x71\x36\x32\x2d\
\x33\x31\x20\x31\x32\x36\x2d\x34\x36\x2e\x35\x54\x34\x38\x30\x2d\
\x34\x34\x30\x71\x36\x36\x20\x30\x20\x31\x33\x30\x20\x31\x35\x2e\
\x35\x54\x37\x33\x36\x2d\x33\x37\x38\x71\x32\x39\x20\x31\x35\x20\
\x34\x36\x2e\x35\x20\x34\x33\x2e\x35\x54\x38\x30\x30\x2d\x32\x37\
\x32\x76\x31\x31\x32\x48\x31\x36\x30\x5a\x6d\x38\x30\x2d\x38\x30\
\x68\x34\x38\x30\x76\x2d\x33\x32\x71\x30\x2d\x31\x31\x2d\x35\x2e\
\x35\x2d\x32\x30\x54\x37\x30\x30\x2d\x33\x30\x36\x71\x2d\x35\x34\
\x2d\x32\x37\x2d\x31\x30\x39\x2d\x34\x30\x2e\x35\x54\x34\x38\x30\
\x2d\x33\x36\x30\x71\x2d\x35\x36\x20\x30\x2d\x31\x31\x31\x20\x31\
\x33\x2e\x35\x54\x32\x36\x30\x2d\x33\x30\x36\x71\x2d\x39\x20\x35\
\x2d\x31\x34\x2e\x35\x20\x31\x34\x74\x2d\x35\x2e\x35\x20\x32\x30\
\x76\x33\x32\x5a\x6d\x32\x34\x30\x2d\x33\x32\x30\x71\x33\x33\x20\
\x30\x20\x35\x36\x2e\x35\x2d\x32\x33\x2e\x35\x54\x35\x36\x30\x2d\
\x36\x34\x30\x71\x30\x2d\x33\x33\x2d\x32\x33\x2e\x35\x2d\x35\x36\
\x2e\x35\x54\x34\x38\x30\x2d\x37\x32\x30\x71\x2d\x33\x33\x20\x30\
\x2d\x35\x36\x2e\x35\x20\x32\x33\x2e\x35\x54\x34\x30\x30\x2d\x36\
\x34\x30\x71\x30\x20\x33\x33\x20\x32\x33\x2e\x35\x20\x35\x36\x2e\
\x35\x54\x34\x38\x30\x2d\x35\x36\x30\x5a\x6d\x30\x2d\x38\x30\x5a\
\x6d\x30\x20\x34\x30\x30\x5a\x22\x2f\x3e\x3c\x2f\x73\x76\x67\x3e\
\
\x00\x00\x01\x2c\
\x3c\
\x73\x76\x67\x20\x78\x6d\x6c\x6e\x73\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x32\
\x34\x22\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x2d\x39\
\x36\x30\x20\x39\x36\x30\x20\x39\x36\x30\x22\x20\x77\x69\x64\x74\
\x68\x3d\x22\x32\x34\x22\x3e\x3c\x70\x61\x74\x68\x20\x64\x3d\x22\
\x4d\x32\x38\x30\x2d\x31\x32\x30\x71\x2d\x33\x33\x20\x30\x2d\x35\
\x36\x2e\x35\x2d\x32\x33\x2e\x35\x54\x32\x30\x30\x2d\x32\x30\x30\
\x76\x2d\x35\x32\x30\x68\x2d\x34\x30\x76\x2d\x38\x30\x68\x32\x30\
\x30\x76\x2d\x34\x30\x68\x32\x34\x30\x76\x34\x30\x68\x32\x30\x30\
\x76\x38\x30\x68\x2d\x34\x30\x76\x35\x32\x30\x71\x30\x20\x33\x33\
\x2d\x32\x33\x2e\x35\x20\x35\x36\x2e\x35\x54\x36\x38\x30\x2d\x31\
\x32\x30\x48\x32\x38\x30\x5a\x6d\x34\x30\x30\x2d\x36\x30\x30\x48\
\x32\x38\x30\x76\x35\x32\x30\x68\x34\x30\x30\x76\x2d\x35\x32\x30\
\x5a\x4d\x33\x36\x30\x2d\x32\x38\x30\x68\x38\x30\x76\x2d\x33\x36\
\x30\x68\x2d\x38\x30\x76\x33\x36\x30\x5a\x6d\x31\x36\x30\x20\x30\
\x68\x38\x30\x76\x2d\x33\x36\x30\x68\x2d\x38\x30\x76\x33\x36\x30\
\x5a\x4d\x32\x38\x30\x2d\x37\x32\x30\x76\x35\x32\x30\x2d\x35\x32\
\x30\x5a\x22\x2f\x3e\x3c\x2f\x73\x76\x67\x3e\
"

qt_resource_name = b"\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x09\
\x00\xa8\xa7\xe7\
\x00\x77\
\x00\x72\x00\x69\x00\x74\x00\x65\x00\x2e\x00\x73\x00\x76\x00\x67\
\x00\x0a\
\x06\xc9\x31\x07\
\x00\x6c\
\x00\x6f\x00\x67\x00\x6f\x00\x75\x00\x74\x00\x2e\x00\x73\x00\x76\x00\x67\
\x00\x0a\
\x0a\x6f\x83\xe7\
\x00\x70\
\x00\x65\x00\x72\x00\x73\x00\x6f\x00\x6e\x00\x2e\x00\x73\x00\x76\x00\x67\
\x00\x0a\
\x0c\xad\x02\x87\
\x00\x64\
\x00\x65\x00\x6c\x00\x65\x00\x74\x00\x65\x00\x2e\x00\x73\x00\x76\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x02\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x30\x00\x00\x00\x00\x00\x01\x00\x00\x01\xf7\
\x00\x00\x00\x4a\x00\x00\x00\x00\x00\x01\x00\x00\x02\xfd\
\x00\x00\x00\x64\x00\x00\x00\x00\x00\x01\x00\x00\x05\x12\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8b\xf8\xf3\x61\xeb\
\x00\x00\x00\x30\x00\x00\x00\x00\x00\x01\x00\x00\x01\xf7\
\x00\x00\x01\x8b\xf8\xf7\x42\x59\
\x00\x00\x00\x4a\x00\x00\x00\x00\x00\x01\x00\x00\x02\xfd\
\x00\x00\x01\x8b\xf8\xf2\x06\x7d\
\x00\x00\x00\x64\x00\x00\x00\x00\x00\x01\x00\x00\x05\x12\
\x00\x00\x01\x8b\xf8\xf0\x7f\xb1\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2


def q_init_resources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


def q_cleanup_resources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


q_init_resources()
