from flask import Flask, render_template
import psutil
import time
import os
path=os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=path)
print(path)
@app.route('/')
def home():
    # Gather system information
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_info = psutil.net_io_counters()
    uptime = time.time() - psutil.boot_time()
    num_processes = len(psutil.pids())
    return render_template('system_info.html', cpu_percent=cpu_percent, memory_percent=memory_percent, disk_percent=disk_percent, network_info=network_info, uptime=uptime, num_processes=num_processes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
