from django import template

register = template.Library()

@register.inclusion_tag('post/_tag.html', takes_context=False)
def render_tag(tag):
    return {
        'tag': tag
    }
