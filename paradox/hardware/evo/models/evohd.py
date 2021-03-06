import logging

from ..panel import Panel_EVOBase

logger = logging.getLogger("PAI").getChild(__name__)


class Panel_EVOHD(Panel_EVOBase):
    mem_map = {
        "labels": {
            "zone": {
                "label_offset": 0,
                "addresses": [
                    range(0x00430, 0x00730, 0x10),  # EVO48
                    range(0x00730, 0x00A30, 0x10),  # EVO96 = EVO48 + 48 zones
                    range(0x062F7, 0x068F7, 0x10),  # EVO192 = EVO96 + 96 zones
                ],
            },
            "pgm": {
                "label_offset": 0,
                "addresses": [range(0x070A6, 0x7486, 0x20)],
                "template": {"on": False, "pulse": False},  # A bit off from EVO 192
            },
            "partition": {
                "label_offset": 0,
                "addresses": [
                    range(0x03A6B, 0x03C17, 0x6B),  # EVO48
                    range(
                        0x03C17, 0x03DC3, 0x6B
                    ),  # EVO96 & EVO192 = EVO48 + 4 partitions
                ],
            },
            "user": {"label_offset": 0, "addresses": [range(0x03E47, 0x04E47, 0x10)]},
            "module": {  # modules
                "label_offset": 0,
                "addresses": [
                    range(0x04E47, 0x05637, 0x10),  # EVO48
                    range(
                        0x05637, 0x05E27, 0x10
                    ),  # EVO96 & EVO192 = EVO48 + 127 modules
                ],
            },
            "door": {"label_offset": 0, "addresses": [range(0x0345C, 0x365C, 0x10)]},
        },
        "definitions": {
            "zone": {
                "addresses": [
                    range(0x01F0, 0x02AE + 2, 2),  # EVO96
                    range(0x60B7, 0x6175 + 2, 2),  # EVO192
                ]
            },
            "partition": {
                "bit_encoded": True,
                "addresses": [[0x39D8]],  # All 8 partitions as bits
            },
            "user": {"addresses": [range(0x0BF0, 0x32EC + 10, 10),]},  # 999 users
        },
    }
