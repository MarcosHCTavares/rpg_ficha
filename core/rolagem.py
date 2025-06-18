# core/rolagem.py

import random
from typing import Optional, Tuple, Dict

class Rolagem:
    @staticmethod
    def rolar_dado(faces: int = 20) -> int:
        """Rola um dado de 'faces' lados."""
        return random.randint(1, faces)

    @staticmethod
    def rolar_ataque(bonus: int = 0, vantagem: Optional[bool] = None) -> Dict[str, int]:
        """
        Rola um teste de ataque ou perícia com possível vantagem ou desvantagem.

        :param bonus: bônus a ser somado no resultado da rolagem
        :param vantagem: True para vantagem, False para desvantagem, None para normal
        :return: dict com valores individuais e total
        """
        if vantagem is True:
            rolagens = [Rolagem.rolar_dado(), Rolagem.rolar_dado()]
            melhor = max(rolagens)
            resultado_total = melhor + bonus
            return {
                "rolagens": rolagens,
                "resultado": melhor,
                "bonus": bonus,
                "total": resultado_total,
                "tipo": "vantagem"
            }
        elif vantagem is False:
            rolagens = [Rolagem.rolar_dado(), Rolagem.rolar_dado()]
            pior = min(rolagens)
            resultado_total = pior + bonus
            return {
                "rolagens": rolagens,
                "resultado": pior,
                "bonus": bonus,
                "total": resultado_total,
                "tipo": "desvantagem"
            }
        else:
            rolagem = Rolagem.rolar_dado()
            resultado_total = rolagem + bonus
            return {
                "rolagens": [rolagem],
                "resultado": rolagem,
                "bonus": bonus,
                "total": resultado_total,
                "tipo": "normal"
            }

    @staticmethod
    def rolagem_texto(resultado: Dict[str, int]) -> str:
        """
        Gera uma string amigável para o resultado da rolagem.

        Exemplo:
         - Normal: "Rolagem: 15 + bônus 3 = 18"
         - Vantagem: "Rolagens: 12 e 17, usa 17 + bônus 3 = 20"
         - Desvantagem: "Rolagens: 8 e 5, usa 5 + bônus 3 = 8"
        """
        tipo = resultado.get("tipo", "normal")
        bonus = resultado.get("bonus", 0)
        total = resultado.get("total", 0)
        rolagens = resultado.get("rolagens", [])

        if tipo == "vantagem":
            return (f"Rolagens: {rolagens[0]} e {rolagens[1]}, "
                    f"usa {max(rolagens)} + bônus {bonus} = {total}")
        elif tipo == "desvantagem":
            return (f"Rolagens: {rolagens[0]} e {rolagens[1]}, "
                    f"usa {min(rolagens)} + bônus {bonus} = {total}")
        else:
            return f"Rolagem: {rolagens[0]} + bônus {bonus} = {total}"


# Teste rápido
if __name__ == "__main__":
    print("Rolagem normal:", Rolagem.rolar_ataque(3))
    print("Rolagem com vantagem:", Rolagem.rolar_ataque(3, vantagem=True))
    print("Rolagem com desvantagem:", Rolagem.rolar_ataque(3, vantagem=False))
