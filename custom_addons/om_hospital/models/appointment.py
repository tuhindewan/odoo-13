from odoo import models, fields, _, api
from datetime import datetime


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def appointment_confirm_button(self):
        for record in self:
            record.state = 'confirm'

    def appointment_done_button(self):
        for record in self:
            record.state = 'done'

    @api.onchange('patient_id')
    def set_patient_blood_group(self):
        for record in self:
            if record.patient_id:
                record.blood_group = record.patient_id.blood_group

    name = fields.Char(string='Appointment ID',
                       required=True,
                       copy=False,
                       readonly=True,
                       index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    blood_group = fields.Selection([
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ],
        string='Blood Group', )
    contact_no = fields.Char(string='Contact Number', related='patient_id.contact_no')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    notes = fields.Text(string="Registration Notes")
    doc_notes = fields.Text(string="Doctor Notes")
    pharmacy_notes = fields.Text(string="Pharmacy Notes")
    appointment_date = fields.Date(string='Date', required=True, default=datetime.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('canceled', 'Canceled')
    ],
        string='Status',
        readonly=True,
        default='draft')
    appointment_lines = fields.One2many('hospital.appointment.line', 'appointment_id',
                                        string='Medicine Lists')
