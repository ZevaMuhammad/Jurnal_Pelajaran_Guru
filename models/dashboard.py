from odoo import models, fields, api

class JurnalMengajarDashboard(models.TransientModel):
    _name = 'jurnal.mengajar.dashboard'
    _description = 'Dashboard Jurnal Mengajar'

    name = fields.Char(string="Title", default="Dashboard Jurnal Mengajar")
    guru_count = fields.Integer(string="Jumlah Guru", compute="_compute_guru_count")
    mata_pelajaran_count = fields.Integer(string="Jumlah Mata Pelajaran", compute="_compute_mata_pelajaran_count")
    jadwal_mengajar_count = fields.Integer(string="Jadwal Mengajar Aktif", compute="_compute_jadwal_mengajar_count")
    daftar_hadir_count = fields.Integer(string="Total Kehadiran", compute="_compute_daftar_hadir_count")

    @api.depends()
    def _compute_guru_count(self):
        for record in self:
            record.guru_count = self.env['jurnal.mengajar.guru'].search_count([])

    @api.depends()
    def _compute_mata_pelajaran_count(self):
        for record in self:
            record.mata_pelajaran_count = self.env['jurnal.mengajar.mata_pelajaran'].search_count([])

    @api.depends()
    def _compute_jadwal_mengajar_count(self):
        for record in self:
            record.jadwal_mengajar_count = self.env['jurnal.mengajar.jadwal'].search_count([])

    @api.depends()
    def _compute_daftar_hadir_count(self):
        for record in self:
            record.daftar_hadir_count = self.env['jurnal.mengajar.hadir'].search_count([])
