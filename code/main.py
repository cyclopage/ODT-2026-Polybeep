#server start up/ main file

import network
import socket
import time
from config import *
from hardware import Buzzer, NeoAnimation, GameServo, Buttons
from game import MODES, play_game
from pages import HTML_PAGE



game_status = 'idle'
selected_mode = None
game_requested = False


def set_status(status):
    global game_status
    game_status = status


#wifi setup

def setup_wifi():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=WIFI_SSID, password=WIFI_PASSWORD, authmode=3)
    
    ip = ap.ifconfig()[0]
    print("Access Point Created!")
    print("SSID:", WIFI_SSID)
    print("IP:", ip)
    
    # Create non-blocking server (crashed otherwise)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 80))
    server.listen(5)
    server.setblocking(False)
    
    return server

    #below section by Claude- wifi connection with HTML page communication
def handle_request(server):
    global game_status, selected_mode, game_requested
    
    try:
        conn, addr = server.accept()
        conn.settimeout(1.0)
        request = conn.recv(1024).decode('utf-8')
        
        if not request:
            conn.close()
            return
        
        # Parse request: "GET /?m=druid HTTP/1.1"
        first_line = request.split('\r\n')[0].split(' ')
        if len(first_line) < 2:
            conn.close()
            return
        
        path = first_line[1]
        
        # Extract query string
        qs = ""
        if '?' in path:
            path, qs = path.split('?', 1)
        
        # Parse query params
        params = {}
        if qs:
            for pair in qs.split('&'):
                if '=' in pair:
                    k, v = pair.split('=', 1)
                    params[k] = v
        
        #route the request
        if not params:
            
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + HTML_PAGE
        
        elif 'status' in params:
            # Status check from phone
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + game_status
        
        elif 'm' in params:
            # character selection
            mode_name = params['m']
            if mode_name in MODES:
                selected_mode = MODES[mode_name]
                game_requested = True
                game_status = 'playing'
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOK"
            else:
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nInvalid"
        
        else:
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nUnknown"
        
        conn.send(response.encode())
        conn.close()
        
    except OSError:
        pass


#main

def main():
    global game_requested, selected_mode, game_status
    
    #setup hardware
    btns = Buttons()
    buz = Buzzer()
    neo = NeoAnimation()
    srv = GameServo()
    
    #setup wifi
    server = setup_wifi()
    
    #main loop
    while True:
        handle_request(server)
        
        if game_requested and selected_mode:
            game_requested = False
            mode = selected_mode
            
            #character feedback
            getattr(buz, f"{mode.name.lower()}_chosen")()
            getattr(neo, f"{mode.name.lower()}_anim")()
            srv.set_character(mode.name.lower())
            
            #play game
            result = play_game(mode, btns, buz, neo, srv, set_status)
            
            time.sleep(3)
            game_status = 'idle'


main()
