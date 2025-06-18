# rolagem.py

import random


class Rolagem:
    """
    Realiza rolagens de dados, testes, ataques e checagens.
    """

    @staticmethod
    def dado(lados, quantidade=1, bonus=0):
        """
        Rola qualquer dado.
        Ex.: dado(6, 2, +3) -> 2d6 +3
        """
        resultados = [random.randint(1, lados) for _ in range(quantidade)]
        total = sum(resultados) + bonus
        return {
            'resultados': resultados,
            'bonus': bonus,
            'total': total
        }

    @staticmethod
    def d20(bonus=0):
        """
        Rola 1d20 + bônus.
        """
        return Rolagem.dado(20, 1, bonus)

    @staticmethod
    def d20_vantagem(bonus=0):
        """
        Rola 2d20, pega o maior (vantagem).
        """
        rolagens = [random.randint(1, 20) for _ in range(2)]
        total = max(rolagens) + bonus
        return {
            'resultados': rolagens,
            'bonus': bonus,
            'total': total,
            'tipo': 'Vantagem'
        }

    @staticmethod
    def d20_desvantagem(bonus=0):
        """
        Rola 2d20, pega o menor (desvantagem).
        """
        rolagens = [random.randint(1, 20) for _ in range(2)]
        total = min(rolagens) + bonus
        return {
            'resultados': rolagens,
            'bonus': bonus,
            'total': total,
            'tipo': 'Desvantagem'
        }

    @staticmethod
    def rolar_ataque(bonus_ataque=0, vantagem=None):
        """
        Faz uma rolagem de ataque:
        - vantagem = True -> vantagem
        - vantagem = False -> desvantagem
        - vantagem = None -> rolagem normal
        """
        if vantagem is True:
            return Rolagem.d20_vantagem(bonus_ataque)
        elif vantagem is False:
            return Rolagem.d20_desvantagem(bonus_ataque)
        else:
            return Rolagem.d20(bonus_ataque)

    @staticmethod
    def rolar_dano(dado, quantidade=1, bonus=0):
        """
        Rola dano. Ex.: d8, quantidade=2, bonus=3 -> 2d8 +3
        """
        lados = int(dado[1:])  # 'd8' -> 8
        return Rolagem.dado(lados, quantidade, bonus)

    @staticmethod
    def rolagem_texto(resultado):
        """
        Formata o resultado da rolagem como texto amigável.
        """
        texto = f"Rolagens: {resultado['resultados']} | Bônus: {resultado['bonus']} | Total: {resultado['total']}"
        if 'tipo' in resultado:
            texto = f"{resultado['tipo']} -> {texto}"
        return texto


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    print("=== Teste de Rolagem ===")

    # D20 normal
    r = Rolagem.d20(+3)
    print("D20 Normal:", Rolagem.rolagem_texto(r))

    # D20 vantagem
    r = Rolagem.d20_vantagem(+5)
    print("D20 Vantagem:", Rolagem.rolagem_texto(r))

    # D20 desvantagem
    r = Rolagem.d20_desvantagem(+2)
    print("D20 Desvantagem:", Rolagem.rolagem_texto(r))

    # Ataque
    r = Rolagem.rolar_ataque(bonus_ataque=6, vantagem=True)
    print("Ataque com vantagem:", Rolagem.rolagem_texto(r))

    # Dano
    r = Rolagem.rolar_dano('d8', quantidade=2, bonus=3)
    print("Dano 2d8+3:", Rolagem.rolagem_texto(r))
