from odoo import models, fields

class JadwalMengajar(models.Model):
    _name = 'jurnal.mengajar.jadwal'
    _description = 'Jadwal Mengajar'

    name = fields.Char(string="Nama Kelas", required=True)
    guru_id = fields.Many2one('jurnal.mengajar.guru', string="Guru", required=True)
    mata_pelajaran_id = fields.Many2one('jurnal.mengajar.mata_pelajaran', string="Mata Pelajaran", required=True)
    tanggal_mulai = fields.Datetime(string="Tanggal Mulai", required=True)
    tanggal_selesai = fields.Datetime(string="Tanggal Selesai", required=True)
