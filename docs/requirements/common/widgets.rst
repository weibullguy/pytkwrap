.. _common_widgets:

==================================
Common Layer — Widget Requirements
==================================

The current implementation does not define separate toolkit-independent
``WidgetMixin``, ``DataWidgetMixin``, or ``PlotWidgetMixin`` classes.
Shared wrapper state and configuration are provided by
``PyTkWrapMixin`` and ``PyTkWrapAttributes``; GTK3-specific behavior is
implemented by the GTK3 mixins and native GTK wrapper classes.

Requirements for the common configuration and value API are maintained
in :ref:`common_mixins`. Compound views such as MatrixView and PlotView
are GTK3-layer features, not common-layer widget mixins.
