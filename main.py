#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
'''
App main function
'''

import sys, os, hashlib
from PySide import QtCore

from PySide.QtGui import QMessageBox

from app.QSingleApplication import QSingleApplication
from utils.common import DummyStream, getAppPath, readFile
from settings import APP_NAME

from app.hub import Hub
from webui import MainWebUI

file_hashes = [
        ('www/scripts/jquery-1.9.1.min.js', '20638E363FCC5152155F24B281303E17DA62DA62D24EF5DCF863B184D9A25734'),
        ('www/scripts/bootstrap.min.js', '5A4A5359110A773BD154DA94C48FFD6A6233A29DFD5A9314555F5AE6C3E47459'),
        ('www/scripts/mustache.min.js', 'E5A64F89FB15EF096845A5038179D09AEB42FFB6D52CD4C329CC5BF7534D5679'),
        ('www/scripts/jquery.qrcode.min.js', 'D0B13B3337DC0A4118C0647E861A4906026662E7DB1E685C0850576C7E7B5938'),
        ('www/scripts/utils.js', '722E759E9AF1197B254A3166159666A001D0648A06464517D4E2719309383512'),
        
        ('www/css/bootstrap.min.css', '568482582B294174BCE30891CB3A3F92AAB5B02300E9E65056258B8D10AD5170'),
        ('www/css/font-awesome.min.css', '08E2DC662D47B0D331279C58FBF70ADDA5D557DAF13CFD44E18F53754492FC8E'),
        
        ('www/css/fonts/fontawesome-webfont.ttf', '7B5A4320FBA0D4C8F79327645B4B9CC875A2EC617A557E849B813918EB733499'),
        ('www/css/fonts/glyphicons-halflings-regular.ttf', 'E395044093757D82AFCB138957D06A1EA9361BDCF0B442D06A18A8051AF57456'),
        ('www/css/fonts/JuliusSansOne-Regular.ttf', 'B540BCAD9283F58955A8DB82D8103B1FD356378F55EC764CDB20D9F5AE749F23'),
    ]

def _check_file_integrity(app):
    ''' Check file integrity to make sure all resources loaded
        to webview won't be modified by an unknown party '''
    for file_name, file_hash in file_hashes:
        file_path = os.path.normpath(os.path.join(app.property("ResPath"), file_name))
        if not os.path.exists(file_path):
            return False
        data = readFile(file_path)
        print( file_path, hashlib.sha256(data).hexdigest().upper() )
        if hashlib.sha256(data).hexdigest().upper() != file_hash:
            return False
    return True


def main():
    if getattr(sys, "frozen", False) and sys.platform in ['win32','cygwin','win64']:
        # and now redirect all default streams to DummyStream:
        sys.stdout = DummyStream()
        sys.stderr = DummyStream()
        sys.stdin = DummyStream()
        sys.__stdout__ = DummyStream()
        sys.__stderr__ = DummyStream()
        sys.__stdin__ = DummyStream()
              
    # Get application path
    app_path = getAppPath()
    if sys.platform == 'darwin' and hasattr(sys, 'frozen'):
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "..", "Resources")))
    else:
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "Resources")))
        
    # Application setup
    
    app = QSingleApplication(sys.argv)
    app.setOrganizationName('ReCoal')
    app.setOrganizationDomain('www.recoal.org')
    app.setApplicationName(APP_NAME)
    app.setProperty("AppPath", app_path)
    app.setProperty("ResPath", resources_path)
    if sys.platform == 'darwin':
        app.setAttribute(QtCore.Qt.AA_DontShowIconsInMenus)
        
    if not _check_file_integrity(app):
        QMessageBox.critical(None, "Application Fatal Error", """<b>File integrity check failed!</b>
                <br><br>This could be a result of unknown (maybe, malicious) action<br> to wallet code files.""")
        app.quit()
    else:
        hub = Hub(app=app)
        ui = MainWebUI(app=app, hub=hub, debug=False)
        hub.setUI(ui)
        app.singleStart(ui)
        
        sys.exit(app.exec_())
