# vision_receive_dict_test.py

import time
import logging

# Importe a classe ProtoVision (ou onde estiver seu receive_dict).
# Ajuste o caminho conforme estiver na sua estrutura.
from V3SProtoComm.core.comm.vision import ProtoVision

def main():
    # Ajuste para DEBUG se quiser mais verbosidade
    logging.basicConfig(level=logging.INFO)

    # Se for o simulador, use IP/porta do simulador (ex: 224.0.0.1:10002).
    # Se for a visão real, use IP/porta da visão (ex: 224.5.23.2:10015).
    # Se 'team_color_yellow' não for relevante, pode deixar True ou False.
    vision = ProtoVision(
        team_color_yellow=True,
        field_data=None,           # Não precisamos de FieldData
        vision_ip='224.5.23.2',    # Ajuste p/ visão real ou simulador
        vision_port=10015
    )

    try:
        while True:
            # Chama diretamente receive_dict() para tentar decodificar o pacote.
            data = vision.receive_dict()

            if data is not None:
                # Se decodificou com sucesso, imprime o dicionário
                print("=== Pacote decodificado ===")
                print(data)
            else:
                print("Nenhum pacote válido decodificado.")

            # Espera meio segundo para não floodar o terminal
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nEncerrando leitura.")

if __name__ == "__main__":
    main()
