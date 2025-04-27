from django import template
from ..models import MenuItem

register = template.Library()

def _build_menu_tree(items, root=None):
    """Строит дерево меню"""
    children = []
    for item in items.filter(parent=root):
        node = {
            'item': item,
            'children': _build_menu_tree(items, item),
        }
        children.append(node)
    return children

@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    all_items = MenuItem.objects.all().order_by('id')
    tree = _build_menu_tree(all_items)
    active_item_ids = set()
    for item in all_items:
        if item.is_active(path):
            active_item_ids.add(item.id)
            while item.parent:
                active_item_ids.add(item.parent.id)
                item = item.parent
                
    return {'tree': tree, 'active_item_ids': active_item_ids}
