# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Planned Price for Products',
    'version': '10.0.1.0.0',
    'category': 'Product',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA,Odoo Community Association (OCA)',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'product',
    ],
    'data': [
        'product_view.xml',
        'wizard/product_update_from_planned_price_wizard_view.xml',
        'data/cron_data.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
    ],
    'test': [
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
