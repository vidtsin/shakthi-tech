# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from docutils.nodes import field


class Applicant_inherit(models.Model):
    _inherit = "hr.applicant"


    native = fields.Char("Native")
    current_city = fields.Char("Present Stay")
    total_exp_yrs = fields.Integer("Total Years of Experience")
    related_experience = fields.Integer('Domain Experience')
    current_salary = fields.Float("Present Salary")   
    current_salary_extra = fields.Char("Current Salary Extra", help="Current Salary of Applicant, extra advantages")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status')
    opinion = fields.Selection([('0', 'Normal'), 
                               ('1', 'Bad'), 
                               ('2', 'Ok'), 
                               ('3', 'Good')], "Opinion", default='0')
    attitude = fields.Selection([('0', 'Normal'), 
                               ('1', 'Bad'), 
                               ('2', 'Ok'), 
                               ('3', 'Good')], "Personality/Attitude", default='0')
    currently_employeed = fields.Selection([('yes','Yes'),
    										('no','No')],'Currently Employeed')
    known_to = fields.Selection([('employee','Employee'),
    							 ('supplier','Supplier'),
    							 ('vendor','Vendor')],'Are you Known to', default='employee')
    known_employee_id = fields.Many2one('hr.employee','Employee Name')
    known_vendor_supplier = fields.Char('Vendor/Supplier Name')
    change_reason = fields.Char('Reason for Change')



class Job(models.Model):

    _inherit = "hr.job"
    _description = "Job Position"


    state = fields.Selection([
        ('draft', 'Draft'),
        ('approval', 'Waiting for Approval'),
        ('recruit', 'Recruitment in Progress'),
        ('open', 'Not Recruiting')
    ], string='Status', readonly=True, required=True, track_visibility='always', copy=False, default='draft', help="Set whether the recruitment process is open or closed for this job position.")
    working_unit = fields.Many2one('work.unit','Working Unit')
    approved_new_employees = fields.Integer('Approved by Management')


    @api.multi
    def set_recruit(self):
        for record in self:
            no_of_recruitment = 1 if record.no_of_recruitment == 0 else record.no_of_recruitment
            record.write({'state': 'draft', 'no_of_recruitment': no_of_recruitment})
        return True

    def send_approval(self):
    	self.state='approval'

    def start_recruit(self):
    	self.state='recruit'