from odoo import models, fields

class GuruPengajar(models.Model):
    _name = 'jurnal.mengajar.guru'
    _description = 'Guru Pengajar'

    name = fields.Char(string="Nama Guru", required=True)
    email = fields.Char(string="Email")
    no_telepon = fields.Char(string="No. Telepon")
    mata_pelajaran_ids = fields.One2many(
        'jurnal.mengajar.mata_pelajaran',
        'guru_id',
        string="Mata Pelajaran yang Diajarkan"
    )

class MataPelajaran(models.Model):
    _name = 'jurnal.mengajar.mata_pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string="Nama Mata Pelajaran", required=True)
    guru_id = fields.Many2one('jurnal.mengajar.guru', string="Guru Pengajar", required=True)
