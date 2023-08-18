# O código deve ser feito dentro do arquivo `challenges/challenge_study_schedule.py`.
# Qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma
# De acordo com o item acima, qual melhor horário para disponibilizar material de estudo
# O horario de entrada e saida é cadastrado no bando de dados
# Lista de tuplas: "permance_period"
# Utilize a estratégia de resolução de problemas "força bruta"
# Função chamada várias vezes com valores diferentes para a VAR "target_time" e serão analisados retornos da função.


def study_schedule(permanence_period, target_time):
# Retorne None se em permanence_period / target_time ;
    if not permanence_period or target_time is None:
        return None

    count = 0

    for period in permanence_period:
        if not isinstance(period, tuple) or len(period) != 2 or period[0] > period[1]:
            return None

        if period[0] <= target_time <= period[1]:
            count += 1

    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_times = [5, 4, 3, 2, 1]

max_count = 0
best_time = None

for time in target_times:
    count = study_schedule(permanence_period, time)
    if count is None:
        print("Permanence period or target time is invalid.")
        break

    if count > max_count:
        max_count = count
        best_time = time

if best_time is not None:
    print(f"O melhor horário é {best_time}, com {max_count} estudantes presentes.")