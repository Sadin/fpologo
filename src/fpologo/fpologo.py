from __future__ import annotations

import xml.etree.ElementTree as et


def main() -> int:
    svg = et.parse('./fedora-horiz_whitebg_test.svg')
    root = svg.getroot()
    for child in root[2][1][1]:
        print(child.get('id'))
        if child.get('id') == 'tspan_main':
            child.text = 'text_main'
            child.set('modified', 'yes')

    svg.write('./fedora-horiz_whitebg_test_modified.svg')
    return 0


if __name__ == '__main__':
    print(main())
