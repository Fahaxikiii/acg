from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *

from mirai import Image

@register(name="ACG", description="ACG PIC", version="0.1", author="Fahaxikiii")
class AcgPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        pass

    async def initialize(self):
        pass

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message
        if msg == "acg":

            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))
            ctx.add_return("reply", [Image(url='https://www.loliapi.com/acg/')])
            ctx.prevent_default()

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message
        if msg == "acg":

            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))
            ctx.add_return("reply", [Image(url='https://www.loliapi.com/acg/'))
            ctx.prevent_default()

    def __del__(self):
        pass
