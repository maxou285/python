
from kivy.app import App

from kivy.properties import StringProperty,  ObjectProperty, DictProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.treeview import TreeViewNode
from kivy.clock import mainthread

import collections

Builder.load_string('''
#:import Window kivy.core.window.Window

<ChooseBdi>:
    auto_dismiss: False
    size: Window.size
    size_hint: None, None
    title: 'BDI Diferenciado'
    tv_proj_bdi: tv_proj_bdi_id

    BoxLayout:
        orientation: 'vertical'
        pading: 5
        spacing: 5

        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1,0.05

            Button:
                size_hint_x: None
                size_x: 40
                text: 'Fechar'
                on_press: root.dismiss()

        GridLayout:
            cols: 3
            rows:1
            size_hint_y: None
            height: self.minimum_height
            spacing: [1,1]
            padding: [1,1]

            CelHeaderChooseBdi:
                text: ''
            CelHeaderChooseBdi:
                text: 'BDI Calculado (%)'
                size_hint_x: None
                width: 150
            CelHeaderChooseBdi:
                text: 'BDI Informado (%)'
                size_hint_x: None
                width: 150

        ScrollView :
            id: scrollviewbdi1
            do_scroll_x: False
            size_hint: 1,0.90
            Scatter:
                do_rotation: False
                do_scale: False
                do_translation: False
                size: tv_proj_bdi_id.size
                size_hint_y: None
                TreeView:
                    id: tv_proj_bdi_id
                    hide_root: False
                    size_hint_y: None
                    width: scrollviewbdi1.width
                    height: self.minimum_height
                    indent_level: 0


<LblRowbdi1@Label>:
    font_size: '12sp'
    size_hint: None,None
    text_size: self.size
    valign: 'center'

<TxtInputTxBdi@TextInput>:
    background_normal:''
    background_color: [1,1,1,1]
    color: [0,0,0,1]
    multiline: False
    font_size: '12sp'
    size_hint: None, None
    size: 100, 27
    text_size: self.size

<CelHeaderChooseBdi@Button>:
    background_normal:''
    background_color: [.9,.9,.9,1]
    color: [0,0,0,1]
    size_hint_y: None
    height: 30
    text_size: self.size
    halign: 'center'
    valign: 'center'

<TreeViewTitleRow>:
    height: desctvbdi_id.height
    GridLayout:
        cols: 5
        size_hint_y: None
        height: self.minimum_height
        
        LblRowbdi1:
            text: root.item if root.item != None else ''
            width: 80
            font_size: '14sp'
            height: desctvbdi_id.height

        LblRowbdi1:
            id: desctvbdi_id
            text: root.descr if root.descr != None else ''
            width: 350
            font_size: '14sp'
            height: self.texture_size[1]


<TreeViewProjRow>:    
    height: descbdi_id.height
    GridLayout:
        cols: 7
        size_hint_y: None
        height: self.minimum_height
        
        LblRowbdi1:
            text: root.item if root.item != None else ''
            width: 80
            height: descbdi_id.height

        LblRowbdi1:
            id: descbdi_id
            text: root.descr if root.descr != None else ''
            size_hint_x: 1
            height: 30 if self.texture_size[1]<30 else self.texture_size[1]
        
        LblRowbdi1:
            text: root.unit if root.unit != None else ''
            width: 60
            height: descbdi_id.height

        CheckBox:
            id: chbox_tx_calc_id
            size_hint_x: None
            width: 50
            group: root.id_group_bdi
            on_active: root.check_active_tax_calc(*args)
        
        TxtInputTxBdi:
            text: root.txbdi_calc if root.txbdi_calc != None else ''
            readonly: True
    
        CheckBox:
            id:chbox_tx_info_id
            size_hint_x: None
            width: 50
            group: root.id_group_bdi
            on_active: root.check_active_tax_info(*args)
        
        TxtInputTxBdi:
            text: root.txbdi_inf if root.txbdi_inf != None else ''
            on_text: root.txbdi_inf = self.text
            on_text: if self.focus: root.update_db()

''')


class ChooseBdi(Popup):
    #class for create interface to register bdi rate
    dic_tv_proj_bdi = DictProperty() #dic with project data
    db_bdi_apply = ObjectProperty() #database conection
    
    def __init__(self, **kwargs):
        super(ChooseBdi, self).__init__(**kwargs)

        self.populate_tree_view_proj()

    @mainthread
    def populate_tree_view_proj(self):
        #populate treeview with project data
        self.tv_proj_bdi.root_options=dict(text='Projeto', font_size='16sp')
            
        for key_plan, data in list(self.dic_tv_proj_bdi.items()):
            #main node
            n1 = self.tv_proj_bdi.add_node(TreeViewTitleRow(id_node=None, item=None, descr=key_plan,
                is_open=True))
            
            #nodes with project items
            for key_line, data2 in list(data.items()):
                ite = data2[0]
                desc = data2[1]
                unid = data2[2]
                id_line = data2[3]
                id_parent = data2[4]
                txbdi_inf_confirm = data2[7]
                
                if data2[5] == None:
                    txbdi_calc = ''
                else:
                    txbdi_calc = str(data2[5]*100)
                
                if data2[6] == None:
                    txbdi_inf = ''
                else:
                    txbdi_inf = str(data2[6]*100)
                
                if key_line[-4:] =='ln_0':
                    #project name node
                    self.tv_proj_bdi.add_node(TreeViewTitleRow(id_node=id_line, item=ite, descr=desc,
                       is_open=True), n1)
                elif unid == None:
                    #titles nodes 
                    parent_node = self.find_parent_node_proj(n1, id_parent)
                    self.tv_proj_bdi.add_node(TreeViewProjRow(id_node=id_line, id_group_bdi=id_line,
                        item=ite, descr=desc,  txbdi_calc= txbdi_calc,  
                        txbdi_inf= txbdi_inf,  txbdi_inf_confirm=txbdi_inf_confirm,  
                        root_db_bdi = self.db_bdi_apply, is_open=True), parent_node) 
                else:
                    #sub-titles nodes 
                    parent_node = self.find_parent_node_proj(n1, id_parent)
                    self.tv_proj_bdi.add_node(TreeViewProjRow(id_node=id_line, id_group_bdi=id_line,
                        item=ite, descr=desc,  unit=unid, txbdi_calc= txbdi_calc,  
                        txbdi_inf= txbdi_inf,  txbdi_inf_confirm=txbdi_inf_confirm, 
                        root_db_bdi = self.db_bdi_apply, is_open=True), parent_node)        

    def find_parent_node_proj(self, n1,  parent_node):
        #looks for the parent node to insert into the treeview
        for n in self.tv_proj_bdi.iterate_all_nodes(node = n1):
            if parent_node == n.id_node:
                break
        return n


class TreeViewProjRow(BoxLayout, TreeViewNode):
    #class for interface treeview row
    id_node = ObjectProperty(None, allownone=True)
    id_group_bdi = StringProperty('')
    item=  StringProperty('', allownone=True)
    descr=  StringProperty('', allownone=True)
    unit= StringProperty('', allownone=True)
    txbdi_calc= StringProperty('', allownone=True)
    txbdi_inf = StringProperty('', allownone=True)
    txbdi_inf_confirm = NumericProperty(allownone=True)
    root_db_bdi = ObjectProperty() #database conection
    
    
    def __init__(self, **kwargs):
        super(TreeViewProjRow,  self).__init__(**kwargs)
        
        self.check_inf_confirm_status()
        self.bind(txbdi_inf_confirm=self.update_db)

    @mainthread
    def check_inf_confirm_status(self):
        #initialize checkboxes
        if self.txbdi_inf_confirm == 1:
            self.ids.chbox_tx_info_id.active = True
        elif self.txbdi_inf_confirm == 0:
            self.ids.chbox_tx_calc_id.active = True
        else:
            self.ids.chbox_tx_info_id.active = False
            self.ids.chbox_tx_calc_id.active = False
    
    def update_db(self, *args):
        #update row in database
        
        print('db_test')

    
    def check_active_tax_info(self,  *args):
        #confirms use of bdi informed
        if args[1] == True:
            self.txbdi_inf_confirm = 1
            self.update_child_node()
            self.update_child_check_box()
        else:
            self.check_non_active()

    def check_active_tax_calc(self,  *args):
        #confirms use of bdi calculated
        if args[1] == True:
            self.txbdi_inf_confirm = 0
            self.update_child_check_box()
        else:
            self.check_non_active()
    
    def check_non_active(self):
        #disables propagation of information from the parent node to the child nodes, when the two checkboxes are unchecked
        if self.ids.chbox_tx_info_id.active == False and self.ids.chbox_tx_calc_id.active== False:
            self.txbdi_inf_confirm = None

    def update_child_node(self):
        #propagates information from parent to child node
        for nod in self.nodes:
            nod.txbdi_inf = self.txbdi_inf
            nod.txbdi_inf_confirm = self.txbdi_inf_confirm

    def update_child_check_box(self):
       #propagates information from parent to child node
        for nod in self.nodes:
            nod.ids.chbox_tx_info_id.active= self.ids.chbox_tx_info_id.active
            nod.ids.chbox_tx_calc_id.active= self.ids.chbox_tx_calc_id.active


class TreeViewTitleRow(BoxLayout, TreeViewNode):
    #class for interface treeview row
    id_node = ObjectProperty(None, allownone=True)
    item=  StringProperty('', allownone=True)
    descr=  StringProperty('', allownone=True)
    
    def __init__(self, **kwargs):
        super(TreeViewTitleRow,  self).__init__(**kwargs)


class ChoiceBDIApp(App):
    def build(self):
        
        dic_bdi = collections.OrderedDict() 
        dic_bdi = {'Plan1': {'1_Plan1_ln_0': ['0', 'Total da Planilha: ', None, '1_Plan1_ln_0', None, 0.33878, None, None],
            '1_Plan1_ln_2': ['1', 'Fundação', None, '1_Plan1_ln_2', '1_Plan1_ln_0', 0.33878, None, None], '1_Plan1_ln_3': ['1.1', 'Escavação', 'm3',
            '1_Plan1_ln_3', '1_Plan1_ln_2', 0.33878, None, None], '1_Plan1_ln_4': ['1.2', 'Aço', 'kg', '1_Plan1_ln_4', '1_Plan1_ln_2', 0.33878, None, None], 
            '1_Plan1_ln_5': ['1.3', 'Engenheiro', 'mês', '1_Plan1_ln_5', '1_Plan1_ln_2', 0.33878, None, None]}}
        
        ch = ChooseBdi()
        ch.dic_tv_proj_bdi = dic_bdi
        
        return ch

ChoiceBDIApp().run()