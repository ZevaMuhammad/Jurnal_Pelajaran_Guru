from odoo import models, fields

class DaftarHadir(models.Model):
    _name = 'jurnal.mengajar.hadir'
    _description = 'Daftar Hadir'

    jadwal_id = fields.Many2one('jurnal.mengajar.jadwal', string="Jadwal", required=True)
    siswa_id = fields.Many2one('res.partner', string="Guru", required=True)
    status_kehadiran = fields.Selection([
        ('hadir', 'Hadir'),
        ('izin', 'Izin'),
        ('alpha', 'Alpha'),
    ], string="Status Kehadiran", required=True)
