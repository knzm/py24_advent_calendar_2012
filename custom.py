# -*- coding: utf-8 -*-

from docutils import nodes


class del_node(nodes.Inline, nodes.TextElement):
    pass


def visit_del_html(self, node):
    self.body.append(self.starttag(node, 'del'))


def depart_del_html(self, node):
    self.body.append('</del>')


def setup(app):
    app.add_node(del_node, html=(visit_del_html, depart_del_html))
    app.add_generic_role('del', del_node)
