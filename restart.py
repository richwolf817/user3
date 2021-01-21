import docker
import test
client = docker.from_env() 

print("cha cha cha")
if 'topograph-cicd' in image: 
    logs = container.logs(until=1800)
    if logs:
        container.restart()

print("happy time")
