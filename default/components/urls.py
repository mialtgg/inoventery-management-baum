from unicodedata import name
from django.urls import path
from components. views import (
base_ui_alerts_view,
base_ui_badges_view,
base_ui_buttons_view,
base_ui_colors_view,
base_ui_cards_view,
base_ui_carousel_view,
base_ui_dropdowns_view,
base_ui_grid_view,
base_ui_images_view,
base_ui_tabs_view,
base_ui_accordions_view,
base_ui_modals_view,
base_ui_offcanvas_view,
base_ui_placeholders_view,
base_ui_progress_view,
base_ui_notifications_view,
base_ui_media_view,
base_ui_embed_video_view,
base_ui_typography_view,
base_ui_lists_view,
base_ui_links_view,
base_ui_general_view,
base_ui_ribbons_view,
base_ui_utilities_view,
adance_ui_sweetalerts_view,
adance_ui_nestable_view,
adance_ui_scrollbar_view,
adance_ui_animation_view,
adance_ui_tour_view,
adance_ui_swiper_view,
adance_ui_ratings_view,
adance_ui_highlight_view,
adance_ui_scrollspy_view,
widgets_view,
forms_elements_view,
forms_select_view,
forms_checkboxs_radios_view,
forms_pickers_view,
forms_masks_view,
forms_advanced_view,
forms_range_sliders_view,
forms_validation_view,
forms_wizard_view,
forms_editors_view,
forms_file_uploads_view,
forms_layouts_view,
forms_select2_view,
tables_basic_view,
tables_gridjs_view,
tables_listjs_view,
tables_datatables_view,
charts_apex_charts_line_view,
charts_apex_charts_area_view,
charts_apex_charts_column_view,
charts_apex_charts_bar_view,
charts_apex_charts_mixed_view,
charts_apex_charts_timeline_view,
charts_apex_charts_candlestick_view,
charts_apex_charts_boxplot_view,
charts_apex_charts_bubble_view,
charts_apex_charts_scatter_view,
charts_apex_charts_heatmap_view,
charts_apex_charts_treemap_view,
charts_apex_charts_pie_view,
charts_apex_charts_radialbar_view,
charts_apex_charts_radar_view,
charts_apex_charts_polar_view,
charts_apex_charts_funnel_view,
charts_apex_charts_rangearea_view,
charts_chartjs_view,
charts_echarts_view,
icons_remix_view,
icons_boxicons_view,
icons_materialdesign_view,
icons_lineawesome_view,
icons_feather_view,
icons_crypto_view,
maps_google_view,
maps_vector_view,
maps_leaflet_view
) 


app_name = 'components'

urlpatterns = [
    #  Base ui
    path('base-ui/alerts', view =base_ui_alerts_view,name='base_ui.alerts'),
    path('base-ui/badges', view =base_ui_badges_view,name='base_ui.badges'),
    path('base-ui/buttons', view =base_ui_buttons_view,name='base_ui.buttons'),
    path('base-ui/colors', view =base_ui_colors_view,name='base_ui.colors'),
    path('base-ui/cards', view =base_ui_cards_view,name='base_ui.cards'),
    path('base-ui/carousel', view =base_ui_carousel_view,name='base_ui.carousel'),
    path('base-ui/dropdowns', view =base_ui_dropdowns_view,name='base_ui.dropdowns'),
    path('base-ui/grid', view =base_ui_grid_view,name='base_ui.grid'),
    path('base-ui/images', view =base_ui_images_view,name='base_ui.images'),
    path('base-ui/tabs', view =base_ui_tabs_view,name='base_ui.tabs'),
    path('base-ui/accordions', view =base_ui_accordions_view,name='base_ui.accordions'),
    path('base-ui/modals', view =base_ui_modals_view,name='base_ui.modals'),
    path('base-ui/offcanvas', view =base_ui_offcanvas_view,name='base_ui.offcanvas'),
    path('base-ui/placeholders', view =base_ui_placeholders_view,name='base_ui.placeholders'),
    path('base-ui/progress', view =base_ui_progress_view,name='base_ui.progress'),
    path('base-ui/notifications', view =base_ui_notifications_view,name='base_ui.notifications'),
    path('base-ui/media', view =base_ui_media_view,name='base_ui.media'),
    path('base-ui/embed_video', view =base_ui_embed_video_view,name='base_ui.embed_video'),
    path('base-ui/typography', view =base_ui_typography_view,name='base_ui.typography'),
    path('base-ui/lists', view =base_ui_lists_view,name='base_ui.lists'),
    path('base-ui/links', view =base_ui_links_view,name='base_ui.links'),
    path('base-ui/general', view =base_ui_general_view,name='base_ui.general'),
    path('base-ui/ribbons', view =base_ui_ribbons_view,name='base_ui.ribbons'),
    path('base-ui/utilities', view =base_ui_utilities_view,name='base_ui.utilities'),
    #  Advance ui
    path('adance-ui/sweetalerts', view =adance_ui_sweetalerts_view,name='adance_ui.sweetalerts'),
    path('adance-ui/nestable', view =adance_ui_nestable_view,name='adance_ui.nestable'),
    path('adance-ui/scrollbar', view =adance_ui_scrollbar_view,name='adance_ui.scrollbar'),
    path('adance-ui/animation', view =adance_ui_animation_view,name='adance_ui.animation'),
    path('adance-ui/tour', view =adance_ui_tour_view,name='adance_ui.tour'),
    path('adance-ui/swiper', view =adance_ui_swiper_view,name='adance_ui.swiper'),
    path('adance-ui/ratings', view =adance_ui_ratings_view,name='adance_ui.ratings'),
    path('adance-ui/highlight', view =adance_ui_highlight_view,name='adance_ui.highlight'),
    path('adance-ui/scrollspy', view =adance_ui_scrollspy_view,name='adance_ui.scrollspy'),
    # Widgets
    path("widgets",view = widgets_view,name="widgets"),
    #Forms
    path("forms/basic-elements",view = forms_elements_view,name="forms.elements"),
    path("forms/select",view = forms_select_view,name="forms.select"),
    path("forms/checkboxs-radios",view = forms_checkboxs_radios_view,name="forms.checkboxs_radios"),
    path("forms/pickers",view = forms_pickers_view,name="forms.pickers"),
    path("forms/input-masks",view = forms_masks_view,name="forms.masks"),
    path("forms/advanced",view = forms_advanced_view,name="forms.advanced"),
    path("forms/range-sliders",view = forms_range_sliders_view,name="forms.range_sliders"),
    path("forms/validation",view = forms_validation_view,name="forms.validation"),
    path("forms/wizard",view = forms_wizard_view,name="forms.wizard"),
    path("forms/editors",view = forms_editors_view,name="forms.editors"),
    path("forms/file-uploads",view = forms_file_uploads_view,name="forms.file_uploads"),
    path("forms/layouts",view = forms_layouts_view,name="forms.layouts"),
    path("forms/select2",view = forms_select2_view,name="forms.select2"),
    #tables
    path("tables/basic-tables",view = tables_basic_view,name="tables.basic"),
    path("tables/gridjs",view = tables_gridjs_view,name="tables.gridjs"),
    path("tables/listjs",view = tables_listjs_view,name="tables.listjs"),
    path("tables/datatables",view = tables_datatables_view,name="tables.datatables"),
    #charts
    path("charts/apex-charts/line",view = charts_apex_charts_line_view,name="charts.apex_charts.line"),
    path("charts/apex-charts/area",view = charts_apex_charts_area_view,name="charts.apex_charts.area"),
    path("charts/apex-charts/column",view = charts_apex_charts_column_view,name="charts.apex_charts.column"),
    path("charts/apex-charts/bar",view = charts_apex_charts_bar_view,name="charts.apex_charts.bar"),
    path("charts/apex-charts/mixed",view = charts_apex_charts_mixed_view,name="charts.apex_charts.mixed"),
    path("charts/apex-charts/timeline",view = charts_apex_charts_timeline_view,name="charts.apex_charts.timeline"),
    path("charts/apex-charts/candlestick",view = charts_apex_charts_candlestick_view,name="charts.apex_charts.candlestick"),
    path("charts/apex-charts/boxplot",view = charts_apex_charts_boxplot_view,name="charts.apex_charts.boxplot"),
    path("charts/apex-charts/bubble",view = charts_apex_charts_bubble_view,name="charts.apex_charts.bubble"),
    path("charts/apex-charts/scatter",view = charts_apex_charts_scatter_view,name="charts.apex_charts.scatter"),
    path("charts/apex-charts/heatmap",view = charts_apex_charts_heatmap_view,name="charts.apex_charts.heatmap"),
    path("charts/apex-charts/treemap",view = charts_apex_charts_treemap_view,name="charts.apex_charts.treemap"),
    path("charts/apex-charts/pie",view = charts_apex_charts_pie_view,name="charts.apex_charts.pie"),
    path("charts/apex-charts/radialbar",view = charts_apex_charts_radialbar_view,name="charts.apex_charts.radialbar"),
    path("charts/apex-charts/radar",view = charts_apex_charts_radar_view,name="charts.apex_charts.radar"),
    path("charts/apex-charts/polar",view = charts_apex_charts_polar_view,name="charts.apex_charts.polar"),
    path("charts/apex-charts/funnel",view = charts_apex_charts_funnel_view,name="charts.apex_charts.funnel"),
    path("charts/apex-charts/rangearea",view = charts_apex_charts_rangearea_view,name="charts.apex_charts.rangearea"),
    path("charts/chartjs",view = charts_chartjs_view,name="charts.chartjs"),
    path("charts/echarts",view = charts_echarts_view,name="charts.echarts"),
    path("icons/remix",view = icons_remix_view,name="icons.remix"),
    path("icons/boxicons",view = icons_boxicons_view,name="icons.boxicons"),
    path("icons/materialdesign",view = icons_materialdesign_view,name="icons.materialdesign"),
    path("icons/lineawesome",view = icons_lineawesome_view,name="icons.lineawesome"),
    path("icons/feather",view = icons_feather_view,name="icons.feather"),
    path("icons/crypto",view = icons_crypto_view,name="icons.crypto"),
    path("maps/google",view = maps_google_view,name="maps.google"),
    path("maps/vector",view = maps_vector_view,name="maps.vector"),
    path("maps/leaflet",view = maps_leaflet_view,name="maps.leaflet"),
]
