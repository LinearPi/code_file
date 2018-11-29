import itchat, time
from itchat.content import TEXT

# itchat.auto_login(enableCmdQR = False)
roomslist = []
name = ''

def chat_login():
    itchat.auto_login()
    # itchat.dump_login_status()

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=n)
    if RoomList is None:
        print("%s group is not found!" % (name))
    else:
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = itchat.get_chatrooms()
    #print(roomslist)
    return roomslist


def main():
    getchatrooms = getchatrooms()
    for i in getchatrooms:
        print(i['NickName'])
        roomslist.append(i['NickName'])

    with open('userTeam.txt', 'a', encoding='utf-8')as f:
        for n in roomslist:
            ChatRoom = itchat.update_chatroom(getroom_message(n), detailedMember=True)
            for i in ChatRoom['MemberList']:
                #print (i['Province']+":",i['NickName'])
                f.write(i['Province']+":"+i['NickName']+'\n')
                print('正在写入           '+i['Province']+":",i['NickName'])
        f.close()

if __name__=="__main__":
    chat_login()