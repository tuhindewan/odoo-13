from odoo import models, fields
from datetime import datetime


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Date', required=True, default=datetime.today())
