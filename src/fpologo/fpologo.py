from __future__ import annotations

import logging
import xml.etree.ElementTree as et


def main() -> int:
    # configure logging module
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # load config

    # svg path
    path = './fedora-horiz_whitebg_test.svg'
    tree = et.parse(path)
    logging.info(f'loading svg from {path}')

    # parse SVG
    root = tree.getroot()
    print(root.attrib)

    logging.info('print child information')
    for child in root[2][1][1]:
        print(child.attrib)
        if child.get('id') == 'tspan_main':
            child.text = 'text_main'
            child.set('modified', 'yes')

    # svg.write('./fedora-horiz_whitebg_test_modified.svg')
    return 0


if __name__ == '__main__':
    print(main())
