#!/usr/bin/env python
from SceneGraph.ui import NodeWidget


SCENEGRAPH_WIDGET_TYPE = 'default'


class DefaultWidget(NodeWidget):
    node_class     = 'dagnode' 
    def __init__(self, dagnode, parent=None):
        super(DefaultWidget, self).__init__(dagnode, parent)