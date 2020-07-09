import discord, json, sys, help


with open("deis.json") as f:
    deis_data = json.loads(f.read())

with open("config.json") as f:
    bot_configuration = json.loads(f.read())


class Sequency(discord.Client):
    def __init__(self):
        super().__init__()
        self._channel = None
        self._message = None
        self._command = None
        self._args = None

    async def handle_oeis(self):
        ...

    async def handle_deis(self):
        ...

    async def handle_discord(self):
        ...

    async def handle_bot(self):
        ...

    async def on_message(self, message):
        self._channel = message.channel
        self._message = message
        self._command = message.content.split(":")[1].split(" ")[0]
        self._args = " ".join(message.content.split(" ")[1:])
        namespace = message.content.split(":")[0]
        if namespace in ["oeis"] + bot_configuration["aliases"]["oeis"]:
            async with message.channel.typing():
                await self.handle_oeis()
        if namespace in ["deis"] + bot_configuration["aliases"]["deis"]:
            async with message.channel.typing():
                await self.handle_deis()
        if namespace in ["discord"] + bot_configuration["aliases"]["discord"]:
            async with message.channel.typing():
                await self.handle_discord()
        if namespace in ["bot"] + bot_configuration["aliases"]["bot"]:
            async with message.channel.typing():
                await self.handle_bot()


def main():
    s = Sequency()
    s.run(sys.argv[1])


if __name__ == '__main__':
    main()
