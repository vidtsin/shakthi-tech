# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from docutils.nodes import field

class Employee(models.Model):

    _inherit = "hr.employee"
    
    emp_code = fields.Char("Sequence")
    working_unit = fields.Many2one('work.unit',"Working Unit")
    blood_group = fields.Many2one('blood.group',"Blood Group")
    grade = fields.Many2one('employee.grade',"Grade")
    religion = fields.Many2one('employee.religion','Religion')
    street_permanent_address = fields.Char("Street")
    street1_permanent_address = fields.Char("Street1")
    city_permanent_address = fields.Char("City")
    state_id_permanent_address = fields.Many2one('res.country.state','State')
    zip_permanent_address = fields.Char('Zip')
    country_id_permanent_address = fields.Many2one('res.country','Country')
    street_present_address = fields.Char("Street")
    street1_present_address = fields.Char("Street1")
    city_present_address = fields.Char("City")
    state_id_present_address = fields.Many2one('res.country.state','State')
    zip_present_address = fields.Char('Zip')
    aadhar_number = fields.Char('Aadhar Number')
    epf_number = fields.Char("EPF No")
    uan_number = fields.Char("UAN No")
    esi_number = fields.Char("ESI No")
    esi_branch = fields.Char("ESI Brance Office")
    esi_dispensary = fields.Char("ESI Dispensary")

    country_id_present_address = fields.Many2one('res.country','Country')
    academic_experience_ids = fields.One2many('hr.experience.academics', 'academic_experience_id', string="Academic Experience")
    professional_experience_ids = fields.One2many('hr.experience.professional', 'professional_experience_id', string="Professional Experience")
    family_information_ids = fields.One2many('family.information', 'family_information_id', string="Family Informations")
    employee_benifits_ids = fields.One2many('employee.benifits', 'employee_benifits_id', string="Benifits")

    @api.model
    def create(self, values):
        values['emp_code'] = self.env['ir.sequence'].next_by_code('hr.employee')
        return super(Employee, self).create(values)


class WorkUnit(models.Model):

	_name = "work.unit"

	name = fields.Char('Unit Name')

class BloodGroup(models.Model):

	_name = 'blood.group'

	name = fields.Char('Blood Group')

class EmployeeReligion(models.Model):

	_name = 'employee.religion'

	name = fields.Char("Religion Name")

    
class AcademicExperiences(models.Model):
    _name = "hr.experience.academics"
    _rec_name = "academic_experience_id"
    
    institution = fields.Char("Institution")
    qualification = fields.Char("Qualification")
    yop = fields.Char("Year of Passing")
    percentage = fields.Char("Percentage Scored")
    academic_experience_id = fields.Many2one('hr.employee', string="Academic Experience Ref")


class ProfessionalExperiences(models.Model):
    _name = "hr.experience.professional"
    _rec_name = "professional_experience_id"
    
    company_name = fields.Char("Company Name")
    designation = fields.Char("Designation")
    year_of_service = fields.Date("Years of Experience")
    professional_experience_id = fields.Many2one('hr.employee', string="Professional Experience Ref")


class FamilyInformations(models.Model):
    _name = "family.information"

    name = fields.Char("Name")
    relationship = fields.Many2one('family.relation',"Relationship")
    family_information_id = fields.Many2one('hr.employee', string="Family Informations Ref")


class EmployeeBenifits(models.Model):
    _name = "employee.benifits"

    name = fields.Char("Name")
    expected_date = fields.Date("Date")
    employee_benifits_id = fields.Many2one('hr.employee', string="Benifits Ref")


class FamilyRelation(models.Model):
    _name = "family.relation"

    name = fields.Char("Name")





		

    