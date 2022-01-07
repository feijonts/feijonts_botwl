from asyncio.tasks import wait
import discord
from discord import colour
from discord.ext import commands
import json
import time
import datetime
from datetime import timedelta
from discord.utils import get

date = datetime.datetime.now()
data = f"[Data]: {date.strftime('%d')}/{date.strftime('%m')}/{date.strftime('%Y')} [Hora]: {date.strftime('%H')}:{date.strftime('%M')}:{date.strftime('%S')}"

config = json.load(open('./config.json'))

client = commands.Bot(command_prefix=config['prefix'])

@client.event
async def on_ready():
    print(config['msgOn'] + "\n" + "prefix: " + config['prefix'])

def printComando(canal, comando, author):
    cmd = comando.split(config['prefix'])[1].split(" ")[0]
    print(f"O {author} usou o comando {cmd} no canal {canal}")

resposta1 = ''


@client.command()
async def whitelist(ctx):
    if ctx.channel.id == config['commandsChannel']:
        await ctx.message.delete()
        guild = ctx.message.guild
        category = discord.utils.get(ctx.guild.categories, name=config['categoria'])
        role = get(guild.roles, id=config['everyone'])
        wlchannel = await guild.create_text_channel(f"whitelist-{ctx.author.name}", category=category)
        await wlchannel.set_permissions(role, view_channel=False)
        await wlchannel.set_permissions(ctx.author, view_channel=True)
        command = await ctx.send(f"<@{ctx.author.id}> sua whitelist foi criada")
        iniciarembed = discord.Embed(
            title = "Flame Evolved Whitelist",
            description = f"<@{ctx.author.id}>, para iniciar sua whitelist digite **iniciar**",
            colour = 15158332
        )
        iniciarembed.set_footer(text='Flame Evolved 2021/2022')
        msg1 = await wlchannel.send(embed = iniciarembed)
        time.sleep(1)
        await command.delete()
        def check(m):
            return m.author.id == ctx.author.id
        iniciar = await client.wait_for('message', check=check)
        await iniciar.delete()
        if iniciar.content == 'iniciar':
            await msg1.delete()
            oitavaembed = discord.Embed(
                title = "Pergunta 1",
                description = "**O que é RDM? (de um Exemplo)**",
                colour = 15158332
            )
            oitavaembed.set_footer(text='Flame Evolved 2021/2022')
            msg2 = await wlchannel.send(embed = oitavaembed)
            resposta8 = await client.wait_for('message', check=check)
            await resposta8.delete()
            await msg2.delete()
            nonaembed = discord.Embed(
                title = "Pergunta 2",
                description = "**O que é CombatLogging? (de um Exemplo)**",
                colour = 15158332
            )
            nonaembed.set_footer(text='Flame Evolved 2021/2022')
            msg3 = await wlchannel.send(embed = nonaembed)
            resposta9 = await client.wait_for('message', check=check)
            await resposta9.delete()
            await msg3.delete()
            decimaembed = discord.Embed(
                title = "Pergunta 3",
                description = "**O que é OOC? (de um Exemplo)**",
                colour = 15158332
            )
            decimaembed.set_footer(text='Flame Evolved 2021/2022')
            msg4 = await wlchannel.send(embed = decimaembed)
            resposta10 = await client.wait_for('message', check=check)
            await resposta10.delete()
            await msg4.delete()
            decimaprimeiraembed = discord.Embed(
                title = "Pergunta 4",
                description = "**O que é DarkRP? (de um Exemplo)**",
                colour = 15158332
            )
            decimaprimeiraembed.set_footer(text='Flame Evolved 2021/2022')
            msg5 = await wlchannel.send(embed = decimaprimeiraembed)
            resposta11 = await client.wait_for('message', check=check)
            await resposta11.delete()
            await msg5.delete()
            decimasegundaembed = discord.Embed(
                title = "Pergunta 5",
                description = "**O que é RP? Role Play! (de um Exemplo)**",
                colour = 15158332
            )
            decimasegundaembed.set_footer(text='Flame Evolved 2021/2022')
            msg6 = await wlchannel.send(embed = decimasegundaembed)
            resposta12 = await client.wait_for('message', check=check)
            await resposta12.delete()
            await msg6.delete()
            decimaterceiraembed = discord.Embed(
                title = "Pergunta 6",
                description = "**É permitido discriminação no servidor? Cite pelo menos 2 exemplos de discriminação!**",
                colour = 15158332
            )
            decimaterceiraembed.set_footer(text='Flame Evolved 2021/2022')
            msg7 = await wlchannel.send(embed = decimaterceiraembed)
            resposta13 = await client.wait_for('message', check=check)
            await resposta13.delete()
            await msg7.delete()
            decimaquartaembed = discord.Embed(
                title = "Pergunta 7",
                description = "**É extremamente proibido qualquer uso de programas externos no servidor, cite exemplos de programas externos que possam causar seu banimento permanente no servidor!**",
                colour = 15158332
            )
            decimaquartaembed.set_footer(text='Flame Evolved 2021/2022')
            msg8 = await wlchannel.send(embed = decimaquartaembed)
            resposta14 = await client.wait_for('message', check=check)
            await resposta14.delete()
            await msg8.delete()
            decimaqquintaembed = discord.Embed(
                title = "Pergunta 8",
                description = "**Se você estiver com uma PISTOLA na loja de roupas, chega dois caras de PISTOLA para te sequestrar, o que você faria?**",
                colour = 15158332
            )
            decimaqquintaembed.set_footer(text='Flame Evolved 2021/2022')
            msg9 = await wlchannel.send(embed = decimaqquintaembed)
            resposta15 = await client.wait_for('message', check=check)
            await resposta15.delete()
            await msg9.delete()
            firstemb = discord.Embed(
                title = "Pergunta 9",
                description = "**Onde são as safe-zones da cidade?**\n\n1 - Concessionária, hospital, mecânica, delegacia, praça e 500m dos farms legais!\n\n2 - Concessionária, hospital, bennys, delegacia, garagem principal e praça e 500m dos farms legais!\n\n3 - Concessionária, hospital, bennys, delegacia, praça, todas garagens e 500m dos farms legais!\n\n4 - Hospital, mecânica, delegacia, garagem!",
                colour = 15158332
            )
            firstemb.set_footer(text='Flame Evolved 2021/2022')
            msg10 = await wlchannel.send(embed = firstemb)
            resposta1 = await client.wait_for('message', check=check)
            await resposta1.delete()
            await msg10.delete()
            segundaembed = discord.Embed(
                title = "Pergunta 10",
                description = "**Qual o número máximo de bandidos à uma loja de conveniência?**\n\n1 - 5 bandidos\n\n2 - 7 bandidos\n\n3 - 4 bandidos\n\n4 - 6 bandidos",
                colour = 15158332
            )
            segundaembed.set_footer(text='Flame Evolved 2021/2022')
            msg11 = await wlchannel.send(embed = segundaembed)
            resposta2 = await client.wait_for('message', check=check)
            await resposta2.delete()
            await msg11.delete()
            terceiraemb = discord.Embed(
                title = "Pergunta 11",
                description = "**Qual o número máximo de policiais à um vanilla?**\n\n1 - 6 policiais\n\n2 - 4 policiais\n\n3 - 5 policiais\n\n4 - 7 policiais",
                colour = 15158332
            )
            terceiraemb.set_footer(text='Flame Evolved 2021/2022')
            msg12 = await wlchannel.send(embed = terceiraemb)
            resposta3 = await client.wait_for('message', check=check)
            await resposta3.delete()
            await msg12.delete()
            quartaembed = discord.Embed(
                title = "Pergunta 12",
                description = "**Qual número mínimo de policiais e bandidos no roubo ao banco fleeca! (com refém)?**\n\n1 - Mínimo: 8 Bandidos / 10 Policiaiss\n\n2 - Mínimo: 9 Bandidos / 11 Policiais\n\n3 - Mínimo: 7 Bandidos / 9 Policiais\n\n4 - Mínimo: 10 Bandidos / 12 Policiais",
                colour = 15158332
            )
            quartaembed.set_footer(text='Flame Evolved 2021/2022')
            msg13 = await wlchannel.send(embed = quartaembed)
            resposta4 = await client.wait_for('message', check=check)
            await resposta4.delete()
            await msg13.delete()
            quintaembed = discord.Embed(
                title = "Pergunta 13",
                description = "**Em relação a roubo ao Teatro, qual alternativa está ERRADA!**\n\n1 - É permitido o roubo da ação com refém!\n\n2 - Não permitido o roubo da ação com refém!\n\n3 - Não necessita de negociação.\n\n4 - É proibido subir em prédio ou subir em algo na intenção de matar!",
                colour = 15158332
            )
            quintaembed.set_footer(text='Flame Evolved 2021/2022')
            msg14 = await wlchannel.send(embed = quintaembed)
            resposta5 = await client.wait_for('message', check=check)
            await resposta5.delete()
            await msg14.delete()
            sextaembed = discord.Embed(
                title = "Pergunta 14",
                description = "**No roubo ao Fort Zancudo, qual tipo de armamento é permitido?**\n\n1 - SMG e Fuzil!\n\n2 - Apenas pistolas!\n\n3 - Pistola e Doze!\n\n4 - Apenas SMG!",
                colour = 15158332
            )
            sextaembed.set_footer(text='Flame Evolved 2021/2022')
            msg15 = await wlchannel.send(embed = sextaembed)
            resposta6 = await client.wait_for('message', check=check)
            await resposta6.delete()
            await msg15.delete()
            setimaembed = discord.Embed(
                title = "Pergunta 15",
                description = "**Quais ações podem ser feitas com refém?**\n\n1 - Banco, joalheria e Loja de Departamento!\n\n2 - Loja de Departamento e Ammunation!\n\n3 - Joalheria e Bancos!\n\n4 - Somente bancos!",
                colour = 15158332
            )
            setimaembed.set_footer(text='Flame Evolved 2021/2022')
            msg16 = await wlchannel.send(embed = setimaembed)
            resposta7 = await client.wait_for('message', check=check)
            await resposta7.delete()
            await msg16.delete()
            embedfinal = discord.Embed(
                title = "FINAL",
                description = "**Você terminou sua whitelist, agora aguarde um staff analiza-la!**",
                colour = 15158332
            )
            embedfinal.set_footer(text='Flame Evolved 2021/2022')
            await wlchannel.send(embed = embedfinal)
            time.sleep(10)
            await wlchannel.delete()
            canalLog = client.get_guild(config['guildID']).get_channel(config['canalLogID'])
            acertos = 0
            if resposta1.content == "1":
                acertos = acertos + 1
            if resposta2.content == "3":
                acertos = acertos + 1
            if resposta3.content == "1":
                acertos = acertos + 1
            if resposta4.content == "1":
                acertos = acertos + 1
            if resposta5.content == "1":
                acertos = acertos + 1
            if resposta6.content == "2":
                acertos = acertos + 1
            if resposta7.content == "3":
                acertos = acertos + 1
            resultadoembemd = discord.Embed(
                title = f"Whitelist {ctx.author.name}",
                description = f"**Multipla escolha: {acertos}/7**\n\n1 - O que é RDM? (de um Exemplo)\nResposta: {resposta8.content}**\n\n2 - O que é CombatLogging? (de um Exemplo)\n**Resposta: {resposta9.content}**\n\n3 - O que é OOC? (de um Exemplo)\n**Reposta: {resposta10.content}**\n\n4 - O que é DarkRP? (de um Exemplo)\n**Resposta: {resposta11.content}**\n\n5 - O que é RP? Role Play! (de um Exemplo)\n**Resposta: {resposta12.content}**\n\n6 - É permitido discriminação no servidor? Cite pelo menos 2 exemplos de discriminação\n**Resposta: {resposta13.content}**\n\n7 - É extremamente proibido qualquer uso de programas externos no servidor, cite exemplos de programas externos que possam causar seu banimento permanente no servidor!\n**Resposta: {resposta14.content}**\n\n8 - Se você estiver com uma PISTOLA na loja de roupas, chega dois caras de PISTOLA para te sequestrar, o que você faria?\n**Reposta: {resposta15.content}\n\nUtilize o comando !aprovar <@{ctx.author.id} > ou !reprovar <@{ctx.author.id} >",
                colour = 15158332
            )
            resultadoembemd.set_footer(text='Flame Evolved 2021/2022')
            await canalLog.send(embed = resultadoembemd)
        else:
            await wlchannel.send(f"<@{ctx.author.id}> palava incorreta, esse canal será deletado em 5 segundos")
            time.sleep(6)
            await wlchannel.delete()
    else:
        await ctx.message.delete()

@client.command()
async def configwl(ctx):
    await ctx.message.delete()
    wlchannel = client.get_guild(config['guildID']).get_channel(config['commandsChannel'])
    embedwl = discord.Embed(
        title = "Flame Evolved Whitelist",
        description = "Para iniciar sua whitelist digite o comando: **!whitelist**",
        colour = 15158332
    )
    embedwl.set_footer(text='Flame Evolved 2021/2022')
    embedwl.set_thumbnail(url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    await wlchannel.send(embed = embedwl)

@client.command()
@commands.has_permissions(manage_roles=True)
async def aprovar(ctx, user: discord.Member):
    await ctx.message.delete()
    wlchannel = client.get_guild(config['guildID']).get_channel(config['canalresultados'])
    embedaprovado = discord.Embed(
        title = "Flame Evolved Whitelist",
        description = f"Parabéns {user}, você acabou de ser aprovado em nosso servidor!\n\nAprovado por: <@{ctx.author.id}>",
        colour = 3066993
    )
    embedaprovado.set_author(name='Flame Evolved',icon_url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embedaprovado.set_thumbnail(url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embedaprovado.set_footer(text='Flame Evolved 2021/2022')
    await wlchannel.send(embed = embedaprovado)
    role = discord.utils.get(user.guild.roles, name=config["nameaprovado"])
    await user.add_roles(role)
    role2 = discord.utils.get(user.guild.roles, name=config["namevisitante"])
    await user.remove_roles(role2)
    embedsucesso = discord.Embed(
        title = "🎉 Flame Evolved Whitelist 🎉",
        description = f"👏 Parabéns <@{user.id}>, você acabou de ser aprovado em nosso servidor! Fique bem antento as regras e boa diversão! 👏",
        colour = 3066993
    )
    embedsucesso.set_thumbnail(url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embedsucesso.set_footer(text='Flame Evolved 2021/2022')
    await user.send(embed = embedsucesso)

@client.command()
@commands.has_permissions(manage_roles=True)
async def reprovar(ctx, user: discord.Member):
    await ctx.message.delete()
    wlchannel = client.get_guild(config['guildID']).get_channel(config['canalresultados'])
    embedreprovado = discord.Embed(
        title = "Flame Evolved Whitelist",
        description = f"Não foi dessa vez {user}, você acabou de ser reprovado em nosso servidor!\n\nReprovado por: <@{ctx.author.id}>",
        colour = 15158332
    )
    embedreprovado.set_author(name='Flame Evolved',icon_url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embedreprovado.set_thumbnail(url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embedreprovado.set_footer(text='Flame Evolved 2021/2022')
    await wlchannel.send(embed = embedreprovado)
    embednegado = discord.Embed(
        title = "Flame Evolved Whitelist",
        description = f"<@{user.id}>, infelizmente você foi reprovado em nossa whitelist, mas isso não significa que não pode tentar mais vezes!",
        colour = 15158332
    )
    embednegado.set_thumbnail(url='https://cdn.discordapp.com/attachments/834203747949215784/887837618342101002/Banner-Flame.png')
    embednegado.set_footer(text='Flame Evolved 2021/2022')
    await user.send(embed = embednegado)

client.run(config['botKey'])