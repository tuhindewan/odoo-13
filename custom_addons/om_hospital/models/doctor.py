from odoo import models, fields, _, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    @api.model
    def create(self, values):
        if values.get('doctor_sec', _('New')) == _('New'):
            values['doctor_sec'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or _('New')
        result = super(HospitalDoctor, self).create(values)
        return result

    doctor_sec = fields.Char(string='Doctor ID',
                             required=True,
                             copy=False,
                             readonly=True,
                             index=True,
                             default=lambda self: _('New'))
    name = fields.Char(string='Name',
                       required=True,
                       track_visibility='always')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              default='male',
                              required=True,
                              string='Gender')
    related_user = fields.Many2one('res.users',
                                   string='Related User',
                                   required=True)
