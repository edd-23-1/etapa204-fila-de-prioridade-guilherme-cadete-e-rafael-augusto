# ATENÇÃO: Não altere o código de arquivo
import os.path
import sys
from pytest import raises
from fila_prioridade import FilaPrioridade


# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    result = fila_prioridade.is_empty()
    expected = True

    assert result == expected


def test_is_empty_false():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(3)
    fila_prioridade.add(1,1)

    result = fila_prioridade.is_empty()
    expected = False

    assert result == expected

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(1)
    fila_prioridade.add(1,1)

    result = fila_prioridade.is_full()
    expected = True

    assert result == expected


def test_is_full_false():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(3)
    fila_prioridade.add(1,1)

    result = fila_prioridade.is_full()
    expected = False

    assert result == expected

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método first()

def test_first_com_item():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()
    fila_prioridade.add(1,1)

    result = (fila_prioridade.first().dado, fila_prioridade.first().prioridade)
    expected = (1,1)

    assert result == expected


def test_first_sem_item():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    result = fila_prioridade.first()
    expected = None

    assert result == expected

# ---- FIM: teste método first()


# ---- INÍCIO: teste método add()

def test_add_em_fila_de_prioridade_cheia():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(1)

    fila_prioridade.add(1,1)

    with raises(Exception):
        fila_prioridade.add(2,2) # deve gerar erro


def test_add_em_fila_de_prioridade_vazia():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    result = fila_prioridade.add(1,2)
    result = fila_prioridade.add(2,2)
    expected = True

    assert result == expected and fila_prioridade.size() == 2


def test_add_em_fila_de_prioridade_para_verificar_ordem_aleatoria():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(10)

    fila_prioridade.add('a', 3)
    fila_prioridade.add('b', 5)
    fila_prioridade.add('c', 1)
    fila_prioridade.add('d', 4)
    fila_prioridade.add('e', 2)
    fila_prioridade.add('f', 3)
    fila_prioridade.add('g', 1)
    fila_prioridade.add('h', 5)

    result = fila_prioridade.display()
    expected = [
        ('b', 5),
        ('h', 5),
        ('d', 4),
        ('a', 3),
        ('f', 3),
        ('e', 2),
        ('c', 1),
        ('g', 1),
    ]

    assert result == expected


def test_add_em_fila_de_prioridade_para_verificar_ordem_crescente():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(10)

    fila_prioridade.add('a', 3)
    fila_prioridade.add('b', 2)
    fila_prioridade.add('c', 1)

    result = fila_prioridade.display()
    expected = [
        ('a', 3),
        ('b', 2),
        ('c', 1),
    ]

    assert result == expected


def test_add_em_fila_de_prioridade_para_verificar_ordem_decrescente():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade(10)

    fila_prioridade.add('a', 1)
    fila_prioridade.add('b', 2)
    fila_prioridade.add('c', 3)

    result = fila_prioridade.display()
    expected = [
        ('c', 3),
        ('b', 2),
        ('a', 1),
    ]

    assert result == expected

# ---- FIM: teste método add()


# ---- INÍCIO: teste método remove()

def test_remove_em_fila_de_prioridade_vazia():

    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    with raises(Exception):
        fila_prioridade.remove() # deve gerar erro


def test_remove_em_fila_de_prioridade_com_item():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    fila_prioridade.add('a', 3)
    fila_prioridade.add('b', 2)
    fila_prioridade.add('c', 1)

    item = fila_prioridade.remove()
    result = (item.dado, item.prioridade)
    expected = ('a', 3)
    assert expected == result

    item = fila_prioridade.remove()
    result = (item.dado, item.prioridade)
    expected = ('b', 2)
    assert expected == result

    item = fila_prioridade.remove()
    result = (item.dado, item.prioridade)
    expected = ('c', 1)
    assert expected == result

# ---- FIM: teste método remove()


# ---- INÍCIO: teste método display()

def test_display_em_fila_de_prioridade_com_elementos_string():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    fila_prioridade.add('a', 3)
    fila_prioridade.add('b', 2)
    fila_prioridade.add('c', 1)

    result = fila_prioridade.display()
    expected = [
        ('a', 3),
        ('b', 2),
        ('c', 1),
    ]

    assert result == expected


def test_display_em_fila_de_prioridade_com_elementos_int():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    fila_prioridade.add(1, 3)
    fila_prioridade.add(2, 2)
    fila_prioridade.add(3, 1)

    result = fila_prioridade.display()
    expected = [
        (1, 3),
        (2, 2),
        (3, 1),
    ]

    assert result == expected

# ---- FIM: teste método display()


# ---- INÍCIO: teste método size()

def test_size_em_fila_de_prioridade_ao_criar_fila_de_prioridade():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    result = fila_prioridade.size()
    expected = 0
    
    assert result == expected


def test_size_em_fila_de_prioridade_ao_inserir_itens():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    fila_prioridade.add(1,2)
    result = fila_prioridade.size()
    expected = 1
    assert result == expected

    fila_prioridade.add(1,2)
    result = fila_prioridade.size()
    expected = 2
    assert result == expected

    fila_prioridade.add(1,2)
    result = fila_prioridade.size()
    expected = 3
    assert result == expected


def test_size_ao_remover_itens():
    try:
        exists = os.path.exists("fila_prioridade.py")
        assert exists == True
    except:
        sys.exit()

    fila_prioridade = FilaPrioridade()

    fila_prioridade.add(1,1)
    fila_prioridade.add(1,1)
    fila_prioridade.add(1,1)

    fila_prioridade.remove()
    result = fila_prioridade.size()
    expected = 2
    assert result == expected

    fila_prioridade.remove()
    result = fila_prioridade.size()
    expected = 1
    assert result == expected

    fila_prioridade.remove()
    result = fila_prioridade.size()
    expected = 0
    assert result == expected

# ---- FIM: teste método size()


