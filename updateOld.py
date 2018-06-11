#!/usr/bin/python
import os , time , sys , shutil,glob, json, re
import string

UM_SVN_ROOT = "svn://10.128.161.92/datacard/SPM/03 Customized Requirements/UM/"
UM_DIST = ""
projectList = ["MW41"]
umData ={}
def svnExport(svn,dist):
    cmdStr = 'svn export --force "%s%s" %s' %(UM_SVN_ROOT,svn,dist)
    print cmdStr
    os.system(cmdStr)

for project in projectList:
  print project
  if os.path.isdir(project):
    shutil.rmtree(project)
  svnExport(project,project)
