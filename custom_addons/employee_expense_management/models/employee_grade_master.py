from odoo import api, fields, models
from odoo.exceptions import UserError,Warning,ValidationError
import datetime

class EmployeeGradeMaster(models.Model):
    _name = "employee.grade"
    
    name = fields.Char("Name")
    employee_grade_ids = fields.One2many("employee.grade.line","employee_grade_id",string="Grade Lines")
    

class EmployeeGradeMasterLine(models.Model):
    _name = "employee.grade.line"    
    
    product_id = fields.Many2one("product.product",string="Product")
    type = fields.Selection([('non_metro','Non Metro'),('metro','Metro')],deafult='non_metro')
    amount = fields.Integer("Amount")
    employee_grade_id = fields.Many2one("employee.grade",string="Employee Grade")