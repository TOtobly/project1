# project1
def avatar_url():
    return 'https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png'

def icon_url():
    return 'https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png'

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='KITH LAX L/S TEE(KH3605-104)',color=6998825)
    embed.set_author(name='Successfully checked out!')
    embed.add_field(name='Store', value='KITH',inline=True)
    embed.add_field(name='Size', value='L',inline=True)
    embed.add_field(name='Profile', value='||tset||',inline=True)
    embed.add_field(name='Order', value='||test||',inline=True)
    embed.add_field(name='Proxy List', value='||test||',inline=True)
    embed.add_field(name='Mode', value='Safe',inline=True)
    embed.set_footer(text='CyberAIO - 14/4/2020 15:03.248 ',icon_url=icon_url())
    embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0094/2252/products/KH3605-104_063.progressive.jpg?v=1571984567')
    webhook.send(embed=embed,avatar_url=avatar_url(),username='CyberAIO',)

send_webhook()
