from wxpy import *
import time
import random

bot = Bot()
gp = bot.groups().search('外出')[0]
larger_gp = bot.groups().search('stgs')[0]
zoey = bot.friends().search('念')[0]
zzh = bot.friends().search('周子涵')[0]
yb = bot.friends().search('Yabin')[0]
apps = []
h = [0]

@bot.register(gp)
def rply(msg):

    if msg.is_at:
        
        if msg.text[0]=='1':
            
            msg.reply('@{} 已收到你的申请，请稍候！'.format(msg.member.name))
            apps.append(msg.member.name)
            fwmsg = '学员{}外出，时间{}。信息：\n{}'.format(msg.member.name, time.ctime(), msg.text)
            zoey.send(fwmsg)
            zzh.send(fwmsg)
            yb.send(fwmsg)
            
        elif msg.text[0]=='2':
            
            msg.reply('@{} 已收到你的申请，请稍候！'.format(msg.member.name)) 
            apps.append(msg.member.name)
            fwmsg = '学员{}签到，时间{}。信息：\n{}'.format(msg.member.name, time.ctime(), msg.text)
            zoey.send(fwmsg)
            zzh.send(fwmsg)
            yb.send(fwmsg)

        else:
            msg.reply('@{} 请使用以下格式进行申请：\n (1/2) @Dub\U0001f43b (申请人(至少2个)) (外出原因)\n谢谢'.format(msg.member.name))

    if msg.type == 'Picture':
    
        msg.forward(zoey)
        msg.forward(zzh)
        msg.forward(yb)

    if msg.text[:4] == 'help':
        msg.reply('@{} 请使用以下格式进行申请：\n (1/2) @Dub\U0001f43b (申请人(至少2个)) (外出原因)\n谢谢'.format(msg.member.name))

@bot.register([yb, zzh, zoey])
def rply(msg):
    
    if (msg.text[0] == 'o' or msg.text[0] == 'O') and (msg.text[1] == 'k' or msg.text[1] == 'K'):

        if (h[0] == len(apps)):
            return('没有更多的申请了。')
        ver = random.randint(10000, 100000)
        ls = apps[h[0]]
        h[0] = h[0] + 1
        
        gp.send('{}的申请已经由{}通过。Have fun!\n验证码：{}\n{}的信息：\n{}'.format(ls, msg.chat.name, ver, msg.chat.name, msg.text[3:]))
        
        zoey.send('{}的申请已经由{}通过。验证码：{}.信息：\n{}'.format(ls, msg.chat.name, ver, msg.text))
        zzh.send('{}的申请已经由{}通过。验证码：{}.信息：\n{}'.format(ls, msg.chat.name, ver, msg.text))
        yb.send('{}的申请已经由{}通过。验证码：{}.信息：\n{}'.format(ls, msg.chat.name, ver, msg.text))

    if (msg.text[0] == 'n' or msg.text[0] == 'N') and (msg.text[1] == 'o' or msg.text[1] == 'O'):
        
        if (h[0] == len(apps)):
            return('没有更多的申请了。')
        ls = apps[h[0]]
        h[0] = h[0] + 1
        
        gp.send('{}的申请已经由{}拒绝。\nThat\'s so sad!\n{}的信息：\n{}'.format(ls, msg.chat.name, msg.chat.name, msg.text[2:]))
        
        zoey.send('{}的申请已经由{}拒绝。\n信息：\n{}'.format(ls, msg.chat.name, msg.text))
        zzh.send('{}的申请已经由{}拒绝。\n信息：\n{}'.format(ls, msg.chat.name, msg.text))
        yb.send('{}的申请已经由{}拒绝。\n信息：\n{}'.format(ls, msg.chat.name, msg.text))

embed()
