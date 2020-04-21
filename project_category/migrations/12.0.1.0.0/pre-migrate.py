from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})

    # Remove a view that was renamed in 26a7e26481bc35306ed9aacfb0d2f26bbf78a37d
    view = env['ir.ui.view'].search([('name', '=', 'project.task.search.type')])
    if view:
        view.unlink()
