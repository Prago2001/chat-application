import csv
import string,random
from core.models import User
from chats.models import Message,Chat
from django.contrib.auth.hashers import make_password
file = open(file='/home/pratik/CodePractice/branch-messaging-app/chat/scripts/data.csv',mode='+r')



def get_user_id():
    reader = csv.reader(file,delimiter=",")
    next(reader)
    ids = set()
    for row in reader:
        ids.add(int(row[0]))
    return ids

def generate_user():
    ids = get_user_id()
    users = {}
    for id in ids:
        username = ''.join(random.choices(string.ascii_uppercase,k=3))
        users[username] = id
    return users

def create_user():
    users = generate_user()
    User.objects.bulk_create([
        User(
            username=username,
            password = make_password('branch12'),
            user_id=user_id,
        ) for username,user_id in users.items()
    ])

def create_chats(agent1,agent2):
    users = User.objects.filter(is_agent=False)
    used_slug = set()
    for user in users:
        slug = random.randint(100,999)
        while slug in used_slug:
            slug = random.randint(100,999)
        used_slug.add(slug)
        chat = Chat.objects.create(
            name=user.username,
            slug=slug
        )
        chat.users.add(user,agent1,agent2)
        chat.save()


def create_messages():
    reader = csv.reader(file,delimiter=",")
    next(reader)
    for row in reader:
        id = int(row[0])
        user = User.objects.get(user_id=id)
        chat = Chat.objects.get(name=user.username)
        msg = Message.objects.create(
            chat=chat,
            user=user,
            content=row[2]
        )
        msg.save()






def run():
    # create_user()
    # agent_1 = User.objects.get(username='agent-1')
    # agent_2 = User.objects.get(username='agent-2')
    # create_chats(agent_1,agent_2)
    # create_messages()
