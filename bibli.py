class Livro:
    __slots__ = ["__titulo", "__autor", "__paginas"]

    total_livros = 0

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.paginas = paginas
        Livro.total_livros += 1

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def paginas(self):
        return self.__paginas 

    @paginas.setter
    def paginas(self, valor):
        if valor > 0:
            self.__paginas = valor
        else:
            print("Número de páginas inválido!")

    def exibir_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    @classmethod
    def exibir_total_livros(cls):
        print(f"Total de livros cadastrados: {cls.total_livros}")


class Leitor:
    __slots__ = ["__nome", "__idade"]

    def __init__(self, nome, idade):
        self.__nome = nome 
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else:
            print("Idade inválida!")

    idade = property(get_idade, set_idade)

    def exibir_leitor(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Acervo:
    __slots__ = ["__livros"]

    def __init__(self):
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def listar_livros(self):
        print("Livros cadastrados no acervo:")
        for livro in self.__livros:
            print("-" * 20)
            livro.exibir_livro()


class Biblioteca:
    __slots__ = ["__nome", "__acervo"]

    def __init__(self, nome):
        self.__nome = nome
        self.__acervo = Acervo()

    @property
    def nome(self):
        return self.__nome

    @property
    def acervo(self):
        return self.__acervo

    def exibir_biblioteca(self):
        print(f"Biblioteca: {self.nome}")
        self.acervo.listar_livros()


class Emprestimo:
    __slots__ = ["__livro", "__leitor"]

    def __init__(self, livro, leitor):
        self.__livro = livro
        self.__leitor = leitor

    @property
    def livro(self):
        return self.__livro

    @property
    def leitor(self):
        return self.__leitor

    def exibir_emprestimo(self):
        print(f"Livro emprestado: {self.livro.titulo}")
        print(f"Leitor: {self.leitor.nome}")


def print_sep():
    print("-" * 40)


# ===========================================================================
# Cadastro dos livros
# ===========================================================================

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
livro2 = Livro("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 400)
livro3 = Livro("O Hobbit", "J. R. R. Tolkien", 336)
livro4 = Livro("A Revolução dos Bichos", "George Orwell", 152)
livro5 = Livro("Extraordinário", "R. J. Palacio", 320)
livro6 = Livro("RE:Zero vol-11 ", "Tappei Nagatsuki.", 472)
livro7 = Livro("As Mil e Uma Noites","coletiva de autor anônimo", 1.306 )

# ==========================================================================
# Cadastro dos leitores
# ==========================================================================

leitor1 = Leitor("Pedro Henrique", 18)
leitor2 = Leitor("Maria Clara", 20)

# ================================================================================
# Biblioteca
# ================================================================================

biblioteca = Biblioteca("Biblioteca Mil e uma Histórias")

biblioteca.acervo.adicionar_livro(livro1)
biblioteca.acervo.adicionar_livro(livro2)
biblioteca.acervo.adicionar_livro(livro3)
biblioteca.acervo.adicionar_livro(livro4)
biblioteca.acervo.adicionar_livro(livro5)
biblioteca.acervo.adicionar_livro(livro6)

# ========================================================================================
# Emprétimos
# ========================================================================================

emprestimo1 = Emprestimo(livro6, leitor1)
emprestimo2 = Emprestimo(livro5, leitor2)

# ========================================================================================
# Exibição dos dados
# ========================================================================================

print_sep()
print("DADOS DA BIBLIOTECA")
biblioteca.exibir_biblioteca()

print_sep()
print("LEITORES")
leitor1.exibir_leitor()
print()
leitor2.exibir_leitor()

print_sep()
print("EMPRÉSTIMOS")
emprestimo1.exibir_emprestimo()
print()
emprestimo2.exibir_emprestimo()

print_sep()
Livro.exibir_total_livros()