from __future__ import annotations

import xml.etree.ElementTree as et


def main() -> int:
    svg = et.parse('fedora-horiz_whitebg_test.svg')
    root = svg.getroot()
    print(root)
    return 0


if __name__ == '__main__':
    print(main())
