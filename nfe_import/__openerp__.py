# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2013  Renato Lima - Akretion                                  #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU General Public License for more details.                                 #
#                                                                             #
#You should have received a copy of the GNU General Public License            #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

{
    'name': 'NFE Import',
    'version': '0.1',
    'category': 'Generic Modules',
    'description': """Implementa a importação de notas fiscais através de
arquivos XML""",
    'author': 'Akretion',
    'license': 'AGPL-3',
    'website': 'http://www.openerpbrasil.org',
    'depends': [
        'nfe',
    ],
    'data': [
        'wizard/akretion_nfe_import_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
}

