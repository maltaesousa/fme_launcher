# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FmeLauncher
                                 A QGIS plugin
 Basic plugin to launch fme script from QGIS
                             -------------------
        begin                : 2017-07-18
        copyright            : (C) 2017 by SITN/OM
        email                : olivier.monod@ne.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FmeLauncher class from file FmeLauncher.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .fme_launcher import FmeLauncher
    return FmeLauncher(iface)
