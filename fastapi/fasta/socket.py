# 导入FastAPI框架和WebSocket相关的类，以及处理WebSocket连接断开的异常
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# 导入用于返回HTML内容的响应类
from fastapi.responses import HTMLResponse

# 导入uvicorn服务器，这是用来运行FastAPI应用的ASGI服务器
import uvicorn

# 从Python标准库导入字典和列表类型提示，以增强代码可读性和类型检查
from typing import Dict, List

# 创建FastAPI应用程序实例
app = FastAPI()

# 存储一对一聊天的连接，键为用户ID（字符串），值为WebSocket连接对象
user_connections: Dict[str, WebSocket] = {}

# 存储一对多聊天的房间信息，键为房间名（字符串），值为包含WebSocket连接对象的列表
room_connections: Dict[str, List[WebSocket]] = {}

# 定义一个包含HTML页面的字符串，这个页面将被用来测试WebSocket功能
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <!-- 表单用于用户输入消息并发送 -->
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <!-- 无序列表用于显示接收到的消息 -->
        <ul id='messages'>
        </ul>
        <!-- JavaScript代码段，用于创建WebSocket连接并处理消息 -->
        <script>
            var ws;
            // 初始化WebSocket连接，根据是用户ID还是一对多房间来决定连接地址
            function initWebSocket(userId, roomId) {
                if (roomId) {
                    ws = new WebSocket(`ws://localhost:8000/ws/room/${roomId}`);
                } else {
                    ws = new WebSocket(`ws://localhost:8000/ws/user/${userId}`);
                }
                // 当从服务器接收到消息时触发此函数，并将消息添加到页面上
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
            }

            // 发送消息的函数，获取用户输入并发送给服务器，然后清空输入框
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()  // 阻止表单默认提交行为
            }
        </script>
    </body>
</html>
"""

# 定义一个GET请求的路由，当访问根路径时返回上述HTML页面
@app.get("/")
async def get():
    return HTMLResponse(content=html, status_code=200)

# 定义一个WebSocket路由，处理一对一聊天连接
@app.websocket("/ws/user/{user_id}")
async def websocket_user_endpoint(websocket: WebSocket, user_id: str):
    # 接受新的WebSocket连接
    await websocket.accept()
    
    # 将新用户添加到一对一聊天连接字典中
    user_connections[user_id] = websocket
    
    try:
        # 开始监听来自客户端的消息
        while True:
            # 等待接收文本消息
            data = await websocket.receive_text()
            
            # 假设消息格式为 "target_user_id message"，解析出目标用户ID和实际消息内容
            target_user_id = data.split()[0]
            message = ' '.join(data.split()[1:])
            
            # 检查目标用户是否存在并发送消息
            if target_user_id in user_connections:
                await user_connections[target_user_id].send_text(f"Message from {user_id}: {message}")
            else:
                await websocket.send_text(f"User {target_user_id} not found.")
    except WebSocketDisconnect:
        # 如果客户端断开了连接，则从一对一聊天连接字典中移除它
        del user_connections[user_id]
        print(f"User {user_id} disconnected")

# 定义一个WebSocket路由，处理一对多聊天（即房间）连接
@app.websocket("/ws/room/{room_id}")
async def websocket_room_endpoint(websocket: WebSocket, room_id: str):
    # 接受新的WebSocket连接
    await websocket.accept()
    
    # 如果房间不存在，则创建它
    if room_id not in room_connections:
        room_connections[room_id] = []
    
    # 将新用户添加到房间的连接列表中
    room_connections[room_id].append(websocket)
    
    try:
        # 开始监听来自客户端的消息
        while True:
            # 等待接收文本消息
            data = await websocket.receive_text()
            
            # 遍历所有属于该房间的用户并将收到的消息广播出去
            for connection in room_connections[room_id]:
                await connection.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        # 如果客户端断开了连接，则从房间的连接列表中移除它
        room_connections[room_id].remove(websocket)
        print(f"Client disconnected from room {room_id}")

# 如果这个文件是作为主程序运行的（而不是被导入），则启动uvicorn服务器
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # 在所有网络接口上监听8000端口