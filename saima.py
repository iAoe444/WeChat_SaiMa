from wxpy import *
import random
import time

groupName = '微信赛马'

bot = Bot(cache_path=True)
ready = False
group = bot.groups().search(groupName)[0]
@bot.register(chats=group,except_self=False)
def print_messages(msg):
    try:
        if msg.text == '赛马':
        	group.send('1.🐴\n2.🐴\n3.🐴\n4.🐴\n5.🐴')
        	global ready
        	ready = True
        elif ready==True and int(msg.text)>0 and int(msg.text)<6:
        	ready = False
        	saima(int(msg.text))
        else:
            print(msg.text)
    except Exception as result:
        print("错误：%s" % result)


def saima(num):
	miles = [20,20,20,20,20]
	display(miles)
	while True:
		time.sleep(1)
		for i in range(len(miles)):
			newmile = miles[i]-random.randint(0,5)
			miles[i] = newmile
			print(miles[i])
		print("\n")
		if min(miles)<0:
			winner = miles.index(min(miles))+1
			group.send(str(winner)+'.🐎')
			group.send(str(winner)+'号获得胜利')
			if num == winner:
				group.send('恭喜你，你赢了')
			else:
				group.send('你输了')
			break;
		else:
			display(miles)

def display(miles):
	group.send('1.'+miles[0]*' '+"🐎\n"+'2.'+miles[1]*' '+"🐎\n"+'3.'+miles[2]*' '+"🐎\n"+'4.'+miles[3]*' '+"🐎\n"+'5.'+miles[4]*' '+"🐎")


embed()