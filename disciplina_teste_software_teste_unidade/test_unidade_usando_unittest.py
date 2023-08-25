import unittest
from livro import Livro, Exemplar
from exceptions import TipoIncorretoException, QuantidadeInvalidaException, AnoInvalidoException

class TesteLivro(unittest.TestCase):

    def test_criar_novo_livro(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

        self.assertEqual(novo_livro.titulo, "The Art of Software Testing")  # add assertion here
        self.assertEqual(novo_livro.autores, ["John Glenford Myers", "Corey Sandler", "Tom Badget"])
        self.assertEqual(novo_livro.ano_publicacao, 1976)

    def test_criar_exemplar_com_livro_incorreto(self):
        exemplar = Exemplar(1, 10, 1, 2023, "Editora")
        with self.assertRaises(TipoIncorretoException):
            exemplar.livro = 2
    
#---------------------------------------------------------------------------------------------------------#
#-------------------------------------Meus testes---------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

    def test_criar_exemplar_com_quantidade_negativa(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.quantidade = -5

    def test_criar_exemplar_com_quantidade_zero(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.quantidade = -2
    
    def test_atualizar_titulo_livro(self):
            livro = Livro("Mobdick", ["Michael"], 1970)
            livro.titulo = "As Cronicas de Narnia"
            self.assertEqual(livro.titulo, "As Cronicas de Narnia")
    
    def test_atualizar_autor_livro(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        livro.autores = ["Max", "Jass"]
        self.assertEqual(livro.autores, ["Max", "Jass"])

    def test_atualizar_anoPublicacao_livro(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        livro.ano_publicacao = 1980
        self.assertEqual(livro.ano_publicacao, 1980)

    def test_atualizar_quantidade_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.quantidade = 10
        self.assertEqual(exemplar.quantidade, 10)

    def test_atualizar_edicao_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.edicao = 4
        self.assertEqual(exemplar.edicao, 4)

    def test_atualizar_ano_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.ano = 2000
        self.assertEqual(exemplar.ano, 2000)

    def test_atualizar_ano_exemplar_ano_negativo(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(AnoInvalidoException):
            exemplar.ano = -1980

    def test_atualizar_ano_exemplar_errado(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(AnoInvalidoException):
            exemplar.ano = 1910

    def test_atualizar_editora_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.editora = "Parnaiba"
        self.assertEqual(exemplar.editora, "Parnaiba")

    def test_adicionar_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.adicionar_exemplares(5)
        self.assertEqual(exemplar.quantidade, 7)

    def test_adicionar_exemplar_errado(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.adicionar_exemplares(0)

    def test_adicionar_exemplar_errado_negativo(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.adicionar_exemplares(-3)

    def test_remover_exemplar(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        exemplar.remover_exemplares(1)
        self.assertEqual(exemplar.quantidade, 1)

    def test_remover_exemplar_errado(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.remover_exemplares(0)

    def test_remover_exemplar_errado_negativo(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar.remover_exemplares(-3)

    def test_criar_exemplar_certo(self):
        livro = Livro("Mobdick", ["Michael"], 1970)
        exemplar = Exemplar(livro, 2, 2, 1970, "Brasil")

        self.assertEqual(exemplar.livro, livro)
        self.assertEqual(exemplar.quantidade, 2)
        self.assertEqual(exemplar.edicao, 2)
        self.assertEqual(exemplar.ano, 1970)
        self.assertEqual(exemplar.editora, "Brasil")
    




# if __name__ == '__main__':
#     unittest.main()
