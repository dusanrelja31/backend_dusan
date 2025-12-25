# backend_dusan

- github initial project
- launch aws ec2 instances
- connect aws ec2
    1. git clone https://github.com/dusanrelja31/backend_dusan.git
    2. sudo apt update
    3. sudo apt install -y python3 python3-venv python3-pip
    4. cd /home/ubuntu/backend_dusan
    5. python3 -m venv venv
    6. source venv/bin/activate
    7. pip install flask requests gunicorn
    8. pip freeze > requirements.txt
        Flask==3.0.0
        gunicorn==21.2.0
        requests==2.32.3
        python-dotenv==1.0.1
    9. pip install -r requirements.txt
    10. sudo nano /etc/systemd/system/backend_dusan.service
        [Unit]
        Description=Flask App on Port 5000
        After=network.target

        [Service]
        User=ubunt
        WorkingDirectory=/home/ubuntubackend_dusan
        Environment="PATH=/home/ubuntu/backend_dusan/venv/bin"
        ExecStart=/home/ubuntu/backend_dusan/venv/bin/python app.py
        Restart=always

        [Install]
        WantedBy=multi-user.target
    11. sudo systemctl daemon-reload
    sudo systemctl enable backend_dusan
    sudo systemctl start backend_dusan.service
    sudo systemctl status backend_dusan.service
