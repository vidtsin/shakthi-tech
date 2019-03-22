from odoo import api, fields, models
from odoo.exceptions import UserError,Warning,ValidationError
import datetime


class EmployeeTraining(models.Model):
    _name = "employee.training"
    _rec_name="sequence"
    
    employee_ids = fields.Many2many('hr.employee',string="Participants")
    sequence = fields.Char('Sequence',readonly=True,copy=False)
    department_id = fields.Many2one('hr.department',string="Department")
    planned_month_id = fields.Many2one('planned.month',string="Planned Month")
    trainer = fields.Selection([('internal','Internal'),('external','External')],default="internal")
    trainer_name = fields.Char("Trainer Name")
    trainer_name_id = fields.Many2one('hr.employee',string="Trainer Name")
    training_topic_id = fields.Many2one('training.topics',string="Training Topics")
    planned_hours = fields.Float('Planned Hours',copy=False)
    date_from = fields.Datetime("Date From",copy=False)
    date_to = fields.Datetime("Date To",copy=False)
    stages = fields.Selection([('new','New'),('in_progress','In Progress'),('feedback','Feedback'),('done','Done')],default='new',copy=False)
    training_line_ids = fields.One2many('employee.training.line','employee_training_id')
    duration = fields.Char("Duration",copy=False)
    effectiveness_of_training = fields.Selection([('0','Poor'),('1','Fair'),('2','Good'),('3','Excellent')],copy=False)
    
    @api.multi
    def move_to_in_progress(self):
        for emp in self.employee_ids:
            line_ids = self.env['employee.training.line'].create({'employee_id':emp.id,
                                                                  'trainer_id':self.trainer_name_id.id,
                                                                  'training_topic_id':self.training_topic_id.id,
                                                                  'date_from':self.date_from,
                                                                  'date_to':self.date_to,
#                                                                   'duration':self.duration,
                                                                  'employee_training_id':self.id
                                                                  })
            print line_ids
        self.stages = 'in_progress'
    
    @api.multi
    def move_to_feedback(self):
        for lines in self.training_line_ids:
            lines.date_from = self.date_from
            lines.date_to = self.date_to
            lines.duration = self.duration
        self.stages = 'feedback' 
    
    @api.multi
    def move_to_done(self):
        self.stages = 'done'

    @api.model
    def create(self, values):
        values['sequence'] = self.env['ir.sequence'].next_by_code('employee.training')                         
        return super(EmployeeTraining, self).create(values)  
    
    @api.constrains('date_from','date_to')
    def _compute_duration(self):
        if self.date_from > self.date_to:
            raise ValidationError("Date To is greater than Date From ") 
        else:
            if self.date_from and self.date_to:
                date_from = datetime.datetime.strptime(self.date_from, "%Y-%m-%d %H:%M:%S")
                date_to = datetime.datetime.strptime(self.date_to, "%Y-%m-%d %H:%M:%S")
                total_hours = (date_to - date_from).total_seconds() / 3600
                self.duration = str(int(total_hours))+" "+'hours'
    
class PlanedMonth(models.Model):
    _name="planned.month"
    
    name = fields.Char("Period Name")
    duration_start_date = fields.Date("Start Date")
    duration_end_date = fields.Date("End Date")
    code = fields.Integer("Code")
    
    
class TrainingTopics(models.Model):
    _name="training.topics"
    
    name = fields.Char("Name")   

class EmployeeTrainingLine(models.Model):
    _name="employee.training.line"
    _rec_name="employee_id"
    
    employee_id = fields.Many2one("hr.employee",string="Employee")   
    trainer_id = fields.Many2one("hr.employee",string="Trainer")
    training_topic_id = fields.Many2one('training.topics',string="Training Topics")
    date_from = fields.Datetime("Date From")
    date_to = fields.Datetime("Date To")
    supervisor_feedback = fields.Char("Supervisors Feedback")
    employee_feedback = fields.Text("Employee Feedback")
    employee_training_id = fields.Many2one("employee.training")
    state = fields.Selection([('new','New'),('done','Done')],default="new")
    duration = fields.Char("Duration")
    
    @api.multi
    def move_to_done(self):
        self.state = 'done'
        
    
    