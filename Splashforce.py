# project1
from discord import Webhook, RequestsWebhookAdapter, Embed



def avatar_url():
    return 'https://pbs.twimg.com/profile_images/917391315746385920/cryapglx_400x400.jpg'

def icon_url():
    return 'https://pbs.twimg.com/profile_images/917391315746385920/cryapglx_400x400.jpg'

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='KITH LAX L/S TEE(KH3605-104)', url='https://cdn.shopify.com/s/files/1/0094/2252/products/KH3605-104_063.progressive.jpg?v=1571984567',color=2061822)
    embed.add_field(name='PID', value='KH3605',inline=True)
    embed.add_field(name='Size', value='L',inline=True)
    embed.add_field(name='Order Number', value='||test||', inline=True)
    embed.add_field(name='Profile', value='||test||',inline=True)
    embed.set_footer(text='Splashforce  14/4/2020 15:03.248 ',icon_url=icon_url())
    webhook.send(embed=embed,avatar_url=avatar_url(),username='Splashforce',)

send_webhook()
