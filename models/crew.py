# models.py

from odoo import models, fields

class Crew(models.Model):
    _name = 'mission.crew'
    _description = 'Modelo para representar la tripulación'

    name = fields.Char(string='Nombre')
    age = fields.Integer(string='Edad')
    rank = fields.Selection([
        ('astronaut', 'Astronauta'),
        ('engineer', 'Ingeniero'),
        ('scientist', 'Científico'),
    ], string='Rango')