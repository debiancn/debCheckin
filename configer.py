#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import config, info, debug, error, INFO, DEBUG
import configparser
import json


class configer:
    """
    parse the configuration from configfile and cmd.
    configFile read from cmd has higher priority.
    """

    def __init__(self):
        self.configFile = "/etc/debCheckin/config.json"
        self.workDir = None
        self.ircChannel = None
        self.ircNick = None
        self.isNotifier = None
        debug("----------------New Instace----------------")

        try:
            self._readConfigFromJson()
        except NoConfigfile as e:
            pass
        except NoConfFromCmd as e:
            pass

    def _readConfigFromJson(self):
        pass

    def _readConfigFromCmd(self):
        pass
