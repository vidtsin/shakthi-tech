from odoo import api, fields, models
from odoo.exceptions import UserError,Warning,ValidationError
import datetime

class EmployeeExpense(models.Model):
    _name = "employee.expense"
    
    employee_id = fields.Many2one("hr.employee",string="Employee")
    employee_grade_id = fields.Many2one(related="employee_id.employee_grade_id",string="Grade")
    city_type = fields.Selection([('non_metro','Non Metro'),('metro','Metro')],deafult='non_metro')
    employee_expense_ids = fields.One2many("employee.expense.line","employee_expense_id",string="Employee Expense")
    state = fields.Selection([('draft','Draft'),
                              ('submit', 'Submitted'),
                              ('approve', 'Approved'),
                              ('post', 'Posted'),
                              ('done', 'Paid'),
                              ('cancel', 'Refused')
                              ], string='Status', index=True, readonly=True, track_visibility='onchange', copy=False, default='draft', required=True,
        help='Expense Report State')
    
    
#     @api.multi
#     def move_to_submited(self):
#         for expense in self.employee_expense_ids:
#             self.
        
    
    
class EmployeeExpenseLine(models.Model):
    _name = "employee.expense.line"
    
    product_id = fields.Many2one("product.product",string="Product")
    unit_price = fields.Float("Unit Price")
    quantity = fields.Integer('Quantity',default=1)
    amount = fields.Integer("Amount")
    employee_expense_id = fields.Many2one("employee.expense")
#     total_amout = fields.

    @api.onchange('product_id')
    def onchange_product_id(self):
        product_list = []
        res = {'domain': {
                        'product_id': "[('id', '!=', False)]",
                        }}
        if self.product_id:
            for product_id in self.employee_expense_id.employee_grade_id.employee_grade_ids:
                print self.product_id
                if self.product_id.id == product_id.id and product_id.type == self._context.get('city_type'):
                    self.unit_price = product_id.amount
#                     self.amount = product_id.amount
                    
                    
        else:   
            for product_id in self.employee_expense_id.employee_grade_id.employee_grade_ids:
                if product_id.type == self._context.get('city_type'):
                    product_list.append(product_id.id)
            res['domain']['product_id'] = "[('id', 'in', %s)]" % product_list
        return res
    
    @api.onchange('quantity','unit_price')
    def onchange_quantity(self):
        self.amount = self.quantity * self.unit_price
        
        
        
        
    