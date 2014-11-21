
from django import template

from classytags.arguments import StringArgument, Argument
from classytags.core import Options
from classytags.helpers import InclusionTag

register = template.Library()


class ShowTree(InclusionTag):

    name = 'show_tree'
    template = 'treelib/dummy.html'

    options = Options(
        Argument('tree', required=True),
        Argument('node', default=None, required=False),
        StringArgument('template', default='treelib/show.html', required=False),
    )

    def get_context(self, context, tree, node, template):
        if node is None:
            nodes = tree.children(tree.root)
        else:
            nodes = tree.children(node.identifier)

        context.update({
            'tree': tree,
            'nodes': nodes,
            'template': template
        })

        return context


register.tag(ShowTree)