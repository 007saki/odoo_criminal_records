from odoo import api, models
from ..ai_chat.ollama_client import get_ai_reply_ollama

class DiscussChannel(models.Model):
    _inherit = "discuss.channel"

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        message = super().message_post(**kwargs)
        visitor = self.livechat_visitor_id
        message_author = message.author_id

        if len(self) == 1 and visitor and message.body:
            if message_author.id == visitor.partner_id.id:
                visitor.sudo()._update_visitor_last_visit()
                ai_reply = get_ai_reply_ollama(message.body)
                if ai_reply:
                    ai_user = self.env['res.partner'].search([('name', '=', 'AI Assistant')], limit=1)
                    if not ai_user:
                        ai_user = self.env.ref("base.partner_root", raise_if_not_found=False)

                    self.message_post(
                        body=ai_reply,
                        author_id=ai_user.id if ai_user else False
                    )
        return message
