import socketio

# Tạo client socket
sio = socketio.Client()

# Kết nối đến server
@sio.event
def connect():
    print("🔗 Kết nối thành công đến server!")

# Lắng nghe tin nhắn từ server
@sio.on('server_message')
def on_message(data):
    print(f"📩 Tin nhắn từ server: {data}\n")

# Xử lý khi mất kết nối
@sio.event
def disconnect():
    print("❌ Đã mất kết nối với server!")

# Kết nối đến Server WebSocket
sio.connect('http://26.228.134.76:8300')

# Gửi tin nhắn đến server
while (True):
    message = input("Nhập tin nhắn của bạn: ")
    sio.emit('socket_message', message)

# Đợi nhận tin nhắn
sio.wait()
