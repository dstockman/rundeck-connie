#!/usr/bin/python

import cherrypy
import os
import json
import sys
import yum

yb = yum.YumBase()
yb.preconf.debuglevel = 0
yb.setCacheDir()
yb.conf.showdupesfromrepos = True
cherrypy.config.update({'server.socket_host': '0.0.0.0'})

class PackageQuery():
  @cherrypy.expose
  def findPackage(self, packageName):
    foundPkgs = list()
    availablePkgs = yb.pkgSack.returnPackages(patterns=[packageName])
    for pkg in availablePkgs:
      foundPkgs.append({'name': str(pkg), 'value': str(pkg)})
    return json.dumps(foundPkgs)

if __name__ == '__main__':
  cherrypy.quickstart(PackageQuery())
