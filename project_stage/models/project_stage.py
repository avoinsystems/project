##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class ProjectStage(models.Model):

    _name = 'project.stage'
    _description = 'Project Stage'
    _order = 'sequence'

    name = fields.Char(
        string='Stage Name',
        required=True,
        translate=True,
    )
    description = fields.Text(
    )
    sequence = fields.Integer(
    )
    fold = fields.Boolean(
        'Folded in Kanban View',
        help='This stage is folded in the kanban view when'
        'there are no records in that stage to display.',
    )
