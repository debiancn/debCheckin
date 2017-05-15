#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess as P
from warchdog.events import FileSystemEventHandler


class Fmonitor(FileSystemEventHandler):
    """
    File monitor
    """

    def __init_(self, directory):
        self.monitorDir = directory
        self.distribution = "stable"

    def on_created(self, event):
        super(Fmonitor, self).on_created(event)
        if not event.is_directory and \
                (event.src_path.endswith("deb") or
                 event.src_path.endswith("dsc")):
            packagename = event.src_path
            try:
                self._pchecker(packagename)
            except Exception as e:
                pass
            else:
                P.run(["aptly", "repo", "add", self.distribution, packagename],
                      check=True)
            finally:
                self._delete(packagename)
        else:
            self._delete(packagename)

    def _pchecker(self, pkgName):
        pass

    def _delete(self, filename):
        try:
            os.remove(filename)
        except OSError as e:
            shutil.rmtree(filename)
