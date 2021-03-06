# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api


class product_template(models.Model):
    _inherit = "product.template"

    @api.model
    def _get_default_code(self):
        return self.env['ir.sequence'].get('product.default_code')

    default_code = fields.Char(
        required=True,
        default=_get_default_code,
        )

    @api.model
    def create(self, vals):
        """
        If we create from template we send default code by context
        """
        default_code = vals.get('default_code', False)
        if default_code:
            return super(product_template, self.with_context(
                default_default_code=default_code)).create(vals)
        return super(product_template, self).create(vals)


class product_product(models.Model):
    _inherit = "product.product"

    @api.model
    def _get_default_code(self):
        return self.env['ir.sequence'].get('product.default_code')

    default_code = fields.Char(
        required=True,
        default=_get_default_code,
        )
