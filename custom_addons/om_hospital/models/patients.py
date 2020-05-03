from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="Patient Name")


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    _rec_name = 'patient_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.depends('patient_age')
    def set_age_group(self):
        for record in self:
            if record.patient_age:
                if record.patient_age < 18:
                    record.age_group = 'minor'
                else:
                    record.age_group = 'major'

    @api.constrains('patient_age')
    def check_age(self):
        for record in self:
            if record.patient_age <= 5:
                raise ValidationError(_("Age must be greater than 5"))

    @api.model
    def create(self, vals):
        if vals.get('patient_seq', _('New')) == _('New'):
            vals['patient_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    def open_patient_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} - {}".format(record.patient_seq, record.patient_name)))
        return result

    patient_seq = fields.Char(string='Patient Sequence',
                              required=True, copy=False,
                              readonly=True,
                              index=True,
                              default=lambda self: _('New'))
    patient_name = fields.Char(string="Name",
                               required=True,
                               track_visibility='always')
    patient_age = fields.Integer(string="Age",
                                 required=True,
                                 track_visibility='always',
                                 default=1)
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')],
                                 string='Age Group',
                                 compute='set_age_group')
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
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        default='male',
        required=True,
        string='Gender')
    contact_no = fields.Char(string='Contact Number',
                             required=True)
    image = fields.Binary(string="Image",
                          required=True)
    notes = fields.Text(string="Notes")
    appointment_count = fields.Integer(string='Appointments',
                                       compute='get_appointment_count')
    doctor = fields.Many2one('hospital.doctor', string='Doctor')


