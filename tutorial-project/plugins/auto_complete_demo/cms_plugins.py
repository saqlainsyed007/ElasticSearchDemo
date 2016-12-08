from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
# from apps.dnn_next_steps.models import


class AutoCompleteDemoPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'Auto Complete Demo'
    render_template = 'auto_complete_demo/auto_complete_demo.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(AutoCompleteDemoPlugin)
