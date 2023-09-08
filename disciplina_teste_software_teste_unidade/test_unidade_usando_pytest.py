import pytest 

from livro import Livro, Exemplar
from exceptions import TipoIncorretoException, AnoInvalidoException, QuantidadeInvalidaException

def test_criar_novo_livro():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

    assert novo_livro.titulo == "The Art of Software Testing"
    assert novo_livro.autores == ["John Glenford Myers", "Corey Sandler", "Tom Badget"]
    assert novo_livro.ano_publicacao == 1976

def test_criar_novo_livro_com_tipo_errado():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
    exemplar = Exemplar(novo_livro, 10, 1, 2023, "editora")
    with pytest.raises(TipoIncorretoException):
        exemplar.livro = 2

#---------------------------------------------------------------------------------------------------------#
#-------------------------------------Meus testes---------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

def test_criar_exemplar_com_quantidade_negativa():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.quantidade = -5

def test_criar_exemplar_com_quantidade_zero():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.quantidade = -2

def test_atualizar_titulo_livro():
    livro = Livro("Mobdick", ["Michael"], 1970)
    livro.titulo = "As Cronicas de Narnia"
    assert livro.titulo == "As Cronicas de Narnia"

def test_atualizar_autor_livro():
    livro = Livro("Mobdick", ["Michael"], 1970)
    livro.autores = ["Max", "Jass"]
    assert livro.autores == ["Max", "Jass"]

def test_atualizar_anoPublicacao_livro():
    livro = Livro("Mobdick", ["Michael"], 1970)
    livro.ano_publicacao = 1980
    assert livro.ano_publicacao == 1980

def test_atualizar_quantidade_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.quantidade = 10
    assert exemplar.quantidade == 10

def test_atualizar_edicao_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.edicao = 4
    assert exemplar.edicao == 4

def test_atualizar_ano_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.ano = 2000
    assert exemplar.ano == 2000

def test_atualizar_ano_exemplar_ano_negativo():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(AnoInvalidoException):
        exemplar.ano = -1980

def test_atualizar_ano_exemplar_errado():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(AnoInvalidoException):
        exemplar.ano = 1910

def test_atualizar_editora_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.editora = "Parnaiba"
    assert exemplar.editora == "Parnaiba"

def test_adicionar_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.adicionar_exemplares(5)
    assert exemplar.quantidade == 7

def test_adicionar_exemplar_errado():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.adicionar_exemplares(0)

def test_adicionar_exemplar_errado_negativo():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.adicionar_exemplares(-3)

def test_remover_exemplar():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    exemplar.remover_exemplares(1)
    assert exemplar.quantidade == 1

def test_remover_exemplar_errado():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.remover_exemplares(0)

def test_remover_exemplar_errado_negativo():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.remover_exemplares(-3)

def test_criar_exemplar_certo():
    livro = Livro("Mobdick", ["Michael"], 1970)
    exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")

    assert exemplar.livro == livro
    assert exemplar.quantidade == 2
    assert exemplar.edicao == 2
    assert exemplar.ano == 1970
    assert exemplar.editora == "Brasil"
