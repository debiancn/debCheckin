#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
import logging
from logging import error, warning


class Configer:
    """
    configuratin parser
    """

    def __init__(self):
        self.config = {
            'configfile': '/etc/debCheckin/config.json',
            'version': '0.1-1',
            'workdir': '/var/lib/debCheckin',
            'daemon': 'start',
            'verbose': False
        }

        self.__readCOnfigFromCmd()

    def __readCOnfigFromCmd(self):
        args = argparse.ArgumentParser()

        args.add_argument('-c', '--config', help='Configuration file')
        args.add_argument('-w', '--workdir', help='Word directory')
        args.add_argument('--version', action='version',
                          version=self.config['version'])
        args.add_argument('-v', '--verbose', action='store_true', default=None,
                          help='verbose mode')
        args.add_argument('-d', '--daemon', help='daemon mode',
                          choices=['start', 'stop', 'restart'])

        config = args.parse_args()

        if config.config is not None:
            self.config['configfile'] = config.config
            self.__readConfigFromJson(config.config)
        else:
            self.__readConfigFromJson(self.config['configfile'])

        if config.workdir is not None:
            self.config['workdir'] = config.workdir

        if config.verbose is not None:
            self.config['verbose'] = config.verbose

        if config.daemon is not None:
            self.config['daemon'] = config.daemon

    def __readConfigFromJson(self, configfile):
        if not os.path.exists(configfile):
            if configfile == self.config['configfile']:
                warning('Cannot find default configuration file {}'.format(
                    configfile
                ))
                return
            else:
                error('Cannot find configuration file {}'.format(configfile))
                sys.exit(1)

        try:
            with open(configfile) as f:
                jconfig = json.loads(f.read())
                self.config['workdir'] = jconfig['workdir']
                self.config['daemon'] = jconfig['daemon']
                self.config['verbose'] = jconfig['verbose']
        except OSError:
            error("error")
            sys.exit(1)

if __name__ == '__main__':
    FORMAT = '%(levelname)s %(asctime)s %(message)s'
    logging.basicConfig(level=logging.ERROR,
                        format=FORMAT)
    conf = Configer()
    print(conf.config['configfile'])
    print(conf.config['workdir'])
    print(conf.config['daemon'])
    print(conf.config['verbose'])
    print(conf.config['version'])
    if conf.config['verbose'] == True:
        print("test ok")
