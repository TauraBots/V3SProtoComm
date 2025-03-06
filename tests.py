import time
import json
import logging
import numpy as np

from core.comm.controls import ProtoControl, ProtoControlThread
from core.command import TeamCommand
from core.comm.referee import RefereeComm
from core.comm.replacer import ReplacerComm
from core.comm.vision import ProtoVision, ProtoVisionThread
from core.data import FieldData
from core import data

logging.basicConfig(level=logging.INFO)

def vectors_angle(vector1, vector2=np.array((1, 0))):
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    return np.arctan2(np.linalg.det([v2, v1]), np.dot(v1, v2))

def test_transmit_robots():
    print("\n=== Teste 1: ProtoControl transmit_robot ===")
    yellow_control = ProtoControl(team_color_yellow=True, control_ip="127.0.0.1", control_port=20011)
    blue_control = ProtoControl(team_color_yellow=False, control_ip="127.0.0.1", control_port=20011)

    current_time = time.time()
    print("Fase 1: 5 segundos de transmissão (robot 0)...")
    while time.time() - current_time < 5:
        blue_control.transmit_robot(0, -10, 10)
        yellow_control.transmit_robot(0, 10, -10)

    current_time = time.time()
    print("Fase 2: 5 segundos de transmissão (robot 1)...")
    while time.time() - current_time < 5:
        blue_control.transmit_robot(1, 10, 10)
        yellow_control.transmit_robot(1, 5, 5)

    current_time = time.time()
    print("Fase 3: 5 segundos de transmissão (robot 2)...")
    while time.time() - current_time < 5:
        blue_control.transmit_robot(2, -5, -5)
        yellow_control.transmit_robot(2, -15, -15)

    for i in range(3):
        blue_control.transmit_robot(i, 0, 0)
        yellow_control.transmit_robot(i, 0, 0)
    print("Teste 1 finalizado.\n")

def test_team_command_update():
    print("\n=== Teste 2: TeamCommand com ProtoControl.update ===")
    team_command = TeamCommand()
    yellow_control = ProtoControl(team_color_yellow=True, team_command=team_command, control_port=20011)
    blue_control = ProtoControl(team_color_yellow=False, team_command=team_command, control_port=20011)

    current_time = time.time()
    team_command.commands[0].left_speed = -10
    team_command.commands[0].right_speed = 10
    print("Fase 1: Atualizando comandos do robô 0 por 5 segundos...")
    while time.time() - current_time < 5:
        blue_control.update()
        yellow_control.update()

    current_time = time.time()
    team_command.commands[1].left_speed = 5
    team_command.commands[1].right_speed = 5
    print("Fase 2: Atualizando comandos do robô 1 por 5 segundos...")
    while time.time() - current_time < 5:
        blue_control.update()
        yellow_control.update()

    current_time = time.time()
    team_command.commands[2].left_speed = -15
    team_command.commands[2].right_speed = -15
    print("Fase 3: Atualizando comandos do robô 2 por 5 segundos...")
    while time.time() - current_time < 5:
        blue_control.update()
        yellow_control.update()

    team_command.reset()
    blue_control.update()
    yellow_control.update()
    print("Teste 2 finalizado.\n")

def test_proto_control_thread():
    print("\n=== Teste 3: ProtoControlThread ===")
    TEST_ROBOT = 0
    WAIT_TIME = 0.5

    team_command = TeamCommand()
    blue_control = ProtoControlThread(team_color_yellow=False, team_command=team_command, control_port=20011)

    team_command.commands[TEST_ROBOT].left_speed = -10
    team_command.commands[TEST_ROBOT].right_speed = 10

    logging.info("Iniciando a thread de controle...")
    blue_control.start()
    time.sleep(WAIT_TIME)

    logging.info("Pausando a thread de controle...")
    blue_control.pause()
    time.sleep(WAIT_TIME)

    logging.info("Retomando a thread de controle...")
    blue_control.resume()
    time.sleep(WAIT_TIME)

    logging.info("Encerrando a thread de controle...")
    blue_control.stop()
    print("Teste 3 finalizado.\n")

# Teste 4: Comunicação com o árbitro via RefereeComm
def test_referee_comm():
    print("\n=== Teste 4: RefereeComm ===")
    referee = RefereeComm()
    print("Aguardando dados do árbitro. Interrompa com Ctrl+C para encerrar este teste.")
    try:
        while True:
            referee_data = referee.receive()
            print(json.dumps(referee_data, indent=4))
            if referee_data:
                print(f"\nEstado do jogo: {referee_data.get('foul')}\n")
                print(f"Tempo do jogo: {referee_data.get('gameHalf')}\n")
                print(f"Time: {referee_data.get('teamcolor')}\n")
            else:
                print("\nNo data received\n")
    except KeyboardInterrupt:
        logging.info("Encerrando teste de RefereeComm.\n")

# Teste 5: Posicionamento com ReplacerComm e RefereeComm
def test_replacer_comm():
    print("\n=== Teste 5: ReplacerComm ===")
    blue_replacer = ReplacerComm(team_color_yellow=False)
    referee = RefereeComm()

    # Configuração inicial do robô zero
    robot_zero = data.EntityData()
    robot_zero.position.x = data.FIELD_LENGTH / 4 - data.ROBOT_SIZE * 1.2
    robot_zero.position.y = -data.ROBOT_SIZE * 0.3

    ball_entrypoint = np.array([data.FIELD_LENGTH / 2, data.GOAL_WIDTH / 2 - data.BALL_RADIUS * 2.6])
    kick_angle = vectors_angle(ball_entrypoint - np.array([robot_zero.position.x, robot_zero.position.y])) * 180 / np.pi
    robot_zero.position.theta = kick_angle

    print("Aguardando estado PENALTY_KICK...")
    try:
        while True:
            game_state = referee.receive().get('foul', 'STOP')
            if game_state == 'PENALTY_KICK':
                blue_replacer.place_team([(robot_zero, 1)])
                print("PENALTY_KICK detectado. Equipe posicionada.")
                break
    except KeyboardInterrupt:
        print("Teste 5 interrompido pelo usuário.")
    print("Teste 5 finalizado.\n")

# Teste 6: Comunicação de visão com ProtoVision
def test_proto_vision():
    print("\n=== Teste 6: ProtoVision ===")
    vision = ProtoVision(team_color_yellow=False)
    print("Recebendo dados de visão. Interrompa com Ctrl+C para encerrar este teste.")
    try:
        counter = 0
        while True:
            vision_data = vision.receive_dict()
            vision_dict = json.dumps(vision_data, indent=4)
            if vision_dict:
                counter += 1
            print(vision_dict)
    except KeyboardInterrupt:
        logging.info("Encerrando teste de ProtoVision.\n")

# Teste 7: Atualização de FieldData via ProtoVision
def test_proto_vision_field():
    print("\n=== Teste 7: ProtoVision com FieldData ===")
    test_field_data = FieldData()
    vision = ProtoVision(team_color_yellow=False, field_data=test_field_data)

    print("FieldData antes da atualização:")
    print(test_field_data)
    vision.update()
    print("FieldData após a atualização:")
    print(test_field_data)
    print("Teste 7 finalizado.\n")

# Teste 8: Visão com thread usando ProtoVisionThread
def test_proto_vision_thread():
    print("\n=== Teste 8: ProtoVisionThread ===")
    test_field_data = FieldData()
    vision = ProtoVisionThread(team_color_yellow=False, field_data=test_field_data)

    print("Iniciando a thread de visão. Interrompa com Ctrl+C para encerrar este teste.")
    vision.start()
    try:
        while True:
            print(test_field_data)
    except KeyboardInterrupt:
        logging.info("Encerrando teste de ProtoVisionThread.\n")

# Função principal com menu para escolher os testes
def main():
    tests = {
        "1": ("ProtoControl transmit_robot", test_transmit_robots),
        "2": ("TeamCommand com ProtoControl.update", test_team_command_update),
        "3": ("ProtoControlThread", test_proto_control_thread),
        "4": ("RefereeComm", test_referee_comm),
        "5": ("ReplacerComm", test_replacer_comm),
        "6": ("ProtoVision", test_proto_vision),
        "7": ("ProtoVision com FieldData", test_proto_vision_field),
        "8": ("ProtoVisionThread", test_proto_vision_thread)
    }

    print("Selecione o teste a ser executado:")
    for key, (desc, _) in tests.items():
        print(f"{key} - {desc}")
    print("all - Executar todos os testes sequencialmente\n")

    escolha = input("Digite o número do teste ou 'all': ").strip()

    if escolha.lower() == "all":
        for key, (desc, func) in tests.items():
            print(f"\nExecutando Teste {key}: {desc}")
            func()
            input("Pressione Enter para continuar para o próximo teste...")
    elif escolha in tests:
        tests[escolha][1]()
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()
