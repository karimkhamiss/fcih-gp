from kivy.uix.listview import ListView, ListItemButton, CompositeListItem
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, AliasProperty, \
    StringProperty, DictProperty, BooleanProperty, StringProperty, OptionProperty
from kivy.app import App


class ExampleApp(App):
    def build(self):
        tuples = zip(map(str, range(10)), map(str, range(10, 20)))

        args_converter = lambda row_index, rec: {'text': rec,
                                                 'size_hint_y': None,
                                                 'height': 25,
                                                 'cls_dicts': [{'cls': ListItemButton,
                                                                'kwargs': {'text': rec[0]}},
                                                               {'cls': ListItemButton,
                                                                'kwargs': {'text': rec[1]}},
                                                               ]}
        list_adapter = ListAdapter(data=tuples,
                                   args_converter=args_converter,
                                   selection_mode='single',
                                   allow_empty_selction=False,
                                   cls=CompositeListItem)
        list_view = ListView(adapter=list_adapter)

        return list_view


if __name__ == '__main__':
    ExampleApp().run()