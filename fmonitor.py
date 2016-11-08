#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from watchdog.observers import Observer
from warchdog.events import FileSystemEventHandler


class ModifyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        pass


class Fmonitor:
    """
    File monitor
    """

    def __init_(self, directory):
        self.__monitorDir = directory
        self.debList = []
        self.dscList = []

    def monitor(self):
        observer = Observer()
        event_handler = ModifyHandler()
        observer.schedule(event_handler, self.__monitorDir)
        observer.start()
