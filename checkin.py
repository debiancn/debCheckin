#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from configer import Configer
from fmonitor import Fmonitor

class Checkin():
    def __init__(self):
        self.distributions = ["stable", "testing", "unstable"]
        self.config = Configer().config
        self.monitors = [];
        for i in self.distributions:
            self.monitors.append(Fmonitor(self.config.workdir+i, i))

if __name__ == "__main__":
    checkin = Checkin()
