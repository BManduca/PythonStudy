"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS
    DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:

     - QUANTIDADE DE NOTAS
     - A MAIOR NOTA
     - A MENOR NOTA
     - A MÉDIA DA TURMA
     - A SITUAÇÃO (OPCIONAL)

     ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO

"""


def notas(*notas, sit=False):
    """
    ==> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS DE UMA MESMA TURMA.
    :param notas: UMA OU MAIS NOTAS DOS ALUNOS DE UMA MESMA TURMA (ACEITA VÁRIAS NOTAS).
    :param sit: VALOR OPCIONAL, OU SEJA, VALOR QUE VAI INDICAR SE DEVE APARECER OU NÃO A SITUAÇÃO DAS NOTAS DA TURMA.
    :return: DICIONÁRIO COM VÁRIAS INFORMAÇÕES SOBRE A SITUAÇÃO ATUAL DA TURMA.
    """

