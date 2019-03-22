from odoo import api, fields, models
from odoo.exceptions import UserError,Warning,ValidationError
import datetime

class Employee(models.Model):
    _inherit = "hr.employee"
    
    employee_grade_id = fields.Many2one("employee.grade",string="Grade")