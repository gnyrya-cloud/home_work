import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize('input_txt, resalt', [('колобок', 'Колобок'), ('coll', 'Coll'), ('Пока', 'Пока')])
def test_positive_capitalize(input_txt, resalt):
    assert string_utils.capitalize(input_txt) == resalt


@pytest.mark.negative
@pytest.mark.parametrize('input_txt, resalt', [('1245', '1245'), ('!coll', '!coll'), ('   ', '   ')])
def test_negative_capitalize(input_txt, resalt):
    assert string_utils.capitalize(input_txt) == resalt


# Тесты для функции trim
@pytest.mark.positive
@pytest.mark.parametrize('input_txt, resalt',
                         [(' стол', 'стол'), ('  coll', 'coll'), ('   пока, привет', 'пока, привет')])
def test_positive_trim(input_txt, resalt):
    assert string_utils.trim(input_txt) == resalt


@pytest.mark.negative
@pytest.mark.parametrize('input_txt, resalt', [('', ''), ('  ', ''), ('     ', '')])
def test_negative_trim(input_txt, resalt):
    assert string_utils.trim(input_txt) == resalt


# Тесты для функции contains
@pytest.mark.positive
@pytest.mark.parametrize('string, synbol, resalt',
                         [('колобок', 'к', True), ('coll', 'l', True), ('Пока', 'у', False), ('нога33', '3', True),
                          ('фонарь, улица', ',', True), ('Ночь. День. Утро', ' ', True)])
def test_positive_contains(string, synbol, resalt):
    assert string_utils.contains(string, synbol) == resalt


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, resalt', [('дом милый дом', '', True), ('', 'а', False), ('', '', True)])
def test_negative_contains(string, symbol, resalt):
    assert string_utils.contains(string, symbol) == resalt


# Тесты для функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize('string, synbol, resalt',
                         [('колобок', 'к', 'олобо'), ('col', 'l', 'co'), ('Пока7', '7', 'Пока'),
                          ('нога33', '3', 'нога'), (' фонарь, улица', ' ', 'фонарь,улица'),
                          ('Ночь. День. Утро', 'Н', 'очь. День. Утро')])
def test_positive_delete_symbol(string, synbol, resalt):
    assert string_utils.delete_symbol(string, synbol) == resalt


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, resalt',
                         [('дом милый дом', 'р', 'дом милый дом'), ('зона', '', 'зона'), ('', 'л', '')])
def test_negative_delete_symbol(string, symbol, resalt):
    assert string_utils.delete_symbol(string, symbol) == resalt
