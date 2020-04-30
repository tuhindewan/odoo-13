from odoo import models, fields, _, api


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Appointment Line Record'

    appointment_id = fields.Many2one('hospital.appointment', 'Appointment Relationship ID')
    medicine_id = fields.Many2one('product.product', string='Medicine', required=True)
    quantity = fields.Integer(string="Quantity")
