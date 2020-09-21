from django import template

register = template.Library()

@register.inclusion_tag('post/_post.html', takes_context=False)
def render_post(post):
    return {
        'post': post
    }
