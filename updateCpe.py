
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os , time , sys , shutil,glob, json, re
import string

UM_SVN_ROOT = "svn://10.128.161.92/datacard/SPM/03 Customized Requirements/UM/"
UM_DIST = ""
projectList = ["HH70","HH40","HH41","MW70","MW71","IK40"]
umData ={}
def svnExport(svn,dist):
    cmdStr = 'svn export --force "%s%s" %s' %(UM_SVN_ROOT,svn,dist)
    print cmdStr
    os.system(cmdStr)

def createJsonFile(data,file):
    fl=open(file+".js", 'w')
    fl.write("var cpe_config = "+json.dumps(data,ensure_ascii=False,indent=2, sort_keys=True))
    fl.close()

def getList(project):
  umData[project]={}
  filelist = os.listdir(project)
  for customName in filelist:
    if os.path.isdir(project+"/"+customName):
      umData[project][customName] ={}
      umlist = os.listdir(project+"/"+customName)
      umData[project][customName]["umlist"] =[]
      for um in umlist:
        um = um.decode('gbk').encode('utf-8')
        if string.find(um,".redirect")!=-1:
          print um.split(".redirect")[0]
          umData[project][customName]["redirect"] = um.split(".redirect")[0]
        else:
          umData[project][customName]["umlist"].append(um)

#shutil.rmtree(UM_DIST)

for project in projectList:
  print project
  if os.path.isdir(project):
    shutil.rmtree(project)
  svnExport(project,project)
  getList(project)

createJsonFile(umData,"cpe_config")