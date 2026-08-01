from flask import Flask, jsonify, request
# โค้ดจำลองสะพานเชื่อมระหว่างหน้าเว็บ HTML กับฮาร์ดแวร์แขนกล
app = Flask(__name__)

@app.route('/robot/command', methods=['POST'])
def control_robot():
    data = request.json
    action = data.get('action')
    
    print(f"[INDUSTRIAL BRIDGE] ได้รับคำสั่งจากหน้าเว็บ: {action}")
    
    # ตรงนี้ท่านประธานสามารถเขียนไลบรารีจริงเชื่อมต่อพอร์ต Serial / Modbus / ROS ได้เลย
    # เช่น serial_port.write(b'MOVE_HOME\n')
    
    if action == 'HOME':
        status = "แขนกลเคลื่อนที่กลับตำแหน่ง Home สำเร็จ"
    elif action == 'PICK_LEFT':
        status = "แขนกลกวาดหยิบชิ้นงานฝั่งซ้ายสำเร็จ"
    elif action == 'EMERGENCY_STOP':
        status = "⚠️ สั่งหยุดฉุกเฉิน (E-STOP) ตัดระบบไฟทันที!"
    else:
        status = f"ดำเนินการคำสั่ง {action} เรียบร้อย"
        
    return jsonify({"status": "success", "message": status})

if __name__ == '__main__':
    print("=== JARVIS PYTHON INDUSTRIAL BRIDGE STARTED ===")
    app.run(host='0.0.0.0', port=5000)