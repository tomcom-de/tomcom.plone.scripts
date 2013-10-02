import argparse
import os
import sys
import logging
import sys
import shutil
import re

from ConfigParser import ConfigParser

parser = argparse.ArgumentParser(description="""Helper script to make a
valid parsable Template from custom i18n stuff""")

parser.add_argument('--search_path',
                    required=True,
                    dest='search_path',
                    help="""Path where to search the msgids""")

parser.add_argument('--template_path',
                    required=True,
                    dest='template_path',
                    help="""The path to write
the template with the found msgids""")

logger = logging.getLogger('tomcomplonescripts')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class Handler:

    def __init__(self, args):
        """ """
        self.args = args

        if not self.args.search_path.endswith(os.sep):
            self.args.search_path += os.sep

        if not os.path.exists(self.args.search_path):
            search_path = self.args.search_path
            msgstr = 'Path does not exist. PATH="%s"' % search_path
            logger.error(msgstr)

    def __call__(self):

        tal = '<div i18n:domain="%(domain)s" i18n:translate="">%(msgstr)s</div>\n'

        string_ = ''
        for path, folders, file_names in os.walk(self.args.search_path):
            for file_name in file_names:

                if file_name.endswith('js'):
                    data = open(path + os.sep + file_name, 'r').read()
                    translations = re.findall(r"\_\((.+?)\)", data)
                    for trans in translations:

                        msgid = re.findall(r"msgid = \'(.+?)\'", trans)
                        if msgid:
                            msgid = msgid[0]

                        domain = re.findall(r"domain = \'(.+?)\'", trans)
                        if domain:
                            domain = domain[0]

                        if msgid and domain:
                            dict_ = {}
                            dict_['msgstr'] = msgid
                            dict_['domain'] = domain
                            string_ += tal % dict_

        open(self.args.template_path, 'w').write(string_)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    args = parser.parse_args()
    handler = Handler(args)
    handler()


if __name__ == '__main__':
    sys.exit(main())
