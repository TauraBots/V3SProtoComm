import time
import logging
import math
from V3SProtoComm.core.data import FieldData
from V3SProtoComm.core.comm.vision import ProtoVisionThread
from V3SProtoComm.core.comm.controls import ProtoControl
from V3SProtoComm.core.command import TeamCommand

def gotoball():
    print("\n=== Gotoball: Ir em direção à bola ===")
    field_data = FieldData()
    vision_thread = ProtoVisionThread(team_color_yellow=False, field_data=field_data)
    print("Iniciando a thread de visão. Interrompa com Ctrl+C para encerrar.")
    vision_thread.start()
    
    team_command = TeamCommand()
    control = ProtoControl(team_color_yellow=False, team_command=team_command, control_port=20011)
    
    desired_robot_index = 0

    k_turn = 10.0        
    k_forward = 50.0      
    stop_distance = 0.1  
    angle_threshold = 0.1 

    try:
        while True:
            ball = field_data.ball
            if field_data.robots and len(field_data.robots) > desired_robot_index:
                selected_robot = field_data.robots[desired_robot_index]
            else:
                selected_robot = None
                
            if ball is not None and selected_robot is not None:
                robot_x = selected_robot.position.x
                robot_y = selected_robot.position.y
                robot_theta = selected_robot.position.theta
                
                ball_x = ball.position.x
                ball_y = ball.position.y
                
                dx = ball_x - robot_x
                dy = ball_y - robot_y
                distance = math.hypot(dx, dy)
                
                angle_to_ball = math.atan2(dy, dx)
                angle_error = angle_to_ball - robot_theta
                angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error)) 
                
                if distance < stop_distance:
                    forward_speed = 0
                    turn_speed = 0
                else:
                    if abs(angle_error) > angle_threshold:
                        forward_speed = 0
                    else:
                        forward_speed = k_forward * distance
                    turn_speed = k_turn * angle_error
                
                left_speed = forward_speed - turn_speed
                right_speed = forward_speed + turn_speed
                
                team_command.commands[desired_robot_index].left_speed = left_speed
                team_command.commands[desired_robot_index].right_speed = right_speed
                
                control.update()
                
                print("=== Controle ===")
                print("Bola -> x: {:.2f}, y: {:.2f}, Distância: {:.2f}".format(ball_x, ball_y, distance))
                print("Robô (índice {}) -> x: {:.2f}, y: {:.2f}, θ: {:.2f}".format(
                    desired_robot_index, robot_x, robot_y, robot_theta))
                print("Ângulo para bola: {:.2f} rad | Erro angular: {:.2f} rad".format(angle_to_ball, angle_error))
                print("Comando -> Esquerda: {:.2f}, Direita: {:.2f}".format(left_speed, right_speed))
            else:
                print("Dados incompletos: bola ou robô não disponível.")
            
            print("-" * 40)
    except KeyboardInterrupt:
        logging.info("Encerrando gotoball.")

if __name__ == '__main__':
    gotoball()
