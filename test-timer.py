import threading

def disconnect():
    print('disconnected')

print('the application started')

connection_timer = threading.Timer(3.0, disconnect)
connection_timer.start()
print('timer started')
# connection_timer.cancel()
# print('timer canceled')
# connection_timer.start()
# print('timer started')

# connection_timer.cancel()
# connection_timer.join()
# connection_timer.setDaemon() # WTF is that ???

print('The application closed')