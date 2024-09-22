from odoo import models, fields
from odoo.exceptions import UserError
class CustomProject(models.Model):
    
    _inherit = 'project.project'

    eee = fields.Char(string="eee")
    # stage = fields.Selection([
    #     ('to_do','To Do '),
    #     ('in_progress','In Progress'),
    #     ('done','Done'),
    #     ('cancelled','Cancelled'),
    #     ('ready_for_test','Ready For Test'),
    #     ('testing','Testing'),
    #     ('business_confirmation','Business Confirmation')
    #     ])
    
    
    
    
    def action_pp(self):
        raise UserError("test succcess")