# project1
from discord import Webhook, RequestsWebhookAdapter, Embed



def avatar_url():
    return 'https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg'

def icon_url():
    return 'https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg'

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Success - kith.com', url='https://cdn.shopify.com/s/files/1/0094/2252/products/KH3605-104_063.progressive.jpg?v=1571984567')
    embed.add_field(name='Size', value='L',inline=True)
    embed.add_field(name='Product', value='KITH LAX L/S TEE', inline=True)
    embed.add_field(name='Delay', value='1000', inline=True)
    embed.add_field(name='Profile', value='||test||', inline=False)
    embed.add_field(name='Tasks', value='15',inline=False)
    embed.set_footer(text='Balkobot',icon_url=icon_url())
    embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0094/2252/products/KH3605-104_063.progressive.jpg?v=1571984567')
    webhook.send(embed=embed,avatar_url=avatar_url(),username='Balkobot',)

send_webhook()
