from odoo import models, fields

class IsiPengajaran(models.Model):
    _name = 'jurnal.mengajar.isi'
    _description = 'Isi Pengajaran'

    name = fields.Char(string="Judul Materi", required=True)
    jadwal_id = fields.Many2one('jurnal.mengajar.jadwal', string="Jadwal Mengajar", required=True)
    guru_id = fields.Many2one('jurnal.mengajar.guru', string="Guru Pengajar", required=True)
    tipe = fields.Selection([
        ('materi', 'Materi'),
        ('tugas', 'Tugas'),
        ('kuis', 'Kuis')
    ], string="Tipe", required=True)
    deskripsi = fields.Text(string="Deskripsi")
    file_materi = fields.Binary(string="File Materi")
    file_materi_name = fields.Char(string="Nama File")

    tanggal_dibuat = fields.Datetime(string="Tanggal Dibuat", default=fields.Datetime.now)
    batas_waktu = fields.Datetime(string="Batas Waktu", help="Hanya untuk tugas atau kuis")
