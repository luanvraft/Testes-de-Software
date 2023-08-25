import unittest
from livro import Livro, Exemplar
from exceptions import TipoIncorretoException

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
    
    def test_criar_exemplar_com_(self):


# if __name__ == '__main__':
#     unittest.main()
