from odoo import models, fields

class EvaluasiPengajaran(models.Model):
    _name = 'jurnal.mengajar.evaluasi'
    _description = 'Evaluasi Pengajaran'

    jadwal_id = fields.Many2one('jurnal.mengajar.jadwal', string="Jadwal", required=True)
    komentar = fields.Text(string="Komentar Evaluasi")
    skor = fields.Integer(string="Skor (1-10)", required=True)
