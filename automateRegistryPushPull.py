import docker

client = docker.from_env()
client.login(username='whoami',password='dummy',registry='https://ewcsltiacr.azurecr.io')
client.login(username='ewcsltiacr')

client.images.pull('ewcsltiacr.azurecr.io/test:1.0')




res=client.api.tag(image='redis:4',repository='ewcsltiacr.azurecr.io/tagimage/redis',tag='4.0')

print(res)

imageList = client.images.list()

count=0

for image in imageList:
    print(image.tags)
    count=count+1

print(count)
