from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Петров'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=250, example='США после гражданской войны'),
    'trailer': fields.String(required=True, max_length=100, example='#'),
    'year': fields.String(required=True, example=2015),
    'rating': fields.String(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='test@ya.ru'),
    'password': fields.String(required=True, max_length=100, example='111111'),
    'name': fields.String(required=True, max_length=100, example='Serg'),
    'surname': fields.String(required=True, example='Merg'),
    'genre': fields.Nested(genre),
})
