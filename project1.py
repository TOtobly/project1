from dhooks import Webhook, Embed

hook = Webhook('https://discordapp.com/api/webhooks/698151737491587122/lWM73-6dEjZWPDq2ufv6ulDV_YcPBll9xtTR3HutPmaOTI5eD9KVNHnJt5f8YQ93OK4k')
embed = Embed()

image1 = 'http://m.imeitou.com/uploads/allimg/180823/3-1PR3150612.jpg'
image2= 'https://cdn.shopify.com/s/files/1/0094/2252/products/KH3769-101_012_900x.jpg?v=1586521199'
image3= 'https://pbs.twimg.com/profile_images/1122983388913242112/UL7r9FE0_400x400.png'
embed = Embed(
    color=0x5CDBF0,
    timestamp='now'
)

embed.set_author(name='Successful checkout!', icon_url=image3)
embed.add_field(name='Site', value='https://kith.com/collections/kith-graphics/products/kith-uprising-sun-tee-white')
embed.add_field(name='profile', value='test')
embed.add_field(name='Task type', value='test')
embed.add_field(name='Size', value='tset')
embed.add_field(name='Mode', value='test')
embed.add_field(name='Region', value='test')
embed.add_field(name='Dalay', value='test')
embed.add_field(name='Order ID', value='test')
embed.add_field(name='Notes', value='Feeling good? Share your success on Twitter https://twitter.com/EveAIO?s=20')

embed.set_footer(text='EveAIO Checkout Logger', icon_url=image3)
embed.set_thumbnail(image2)

hook.send(embed=embed)