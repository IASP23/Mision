# models.py

from odoo import models, fields

class Spaceship(models.Model):
    _name = 'mission.spaceship'
    _description = 'Modelo para representar la nave espacial'

    name = fields.Char(string='Nombre')
    capacity = fields.Integer(string='Capacidad')
    fuel_level = fields.Float(string='Nivel de combustible')

