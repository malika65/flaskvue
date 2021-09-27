(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[4],{c095:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[t.showHeader?[a("q-card",{staticClass:"q-pa-md q-mb-md no-border-radius ",attrs:{bordered:"",flat:""}},[a("div",{staticClass:"container-fluid"},[a("div",{staticClass:"row justify-between q-col-gutter-md"},[a("div",{staticClass:"col "},[a("div",{staticClass:"text-h6 text-bold record-title"},[t._v(t._s(t.$t("user")))])]),a("div",{staticClass:"col-md-auto col-12 "},[a("q-btn",{staticClass:"full-width",attrs:{rounded:!1,size:"",color:"primary","no-caps":"",unelevated:"",to:"/user/add"}},[a("q-icon",{attrs:{name:"add"}}),t._v("                                \n                            "+t._s(t.$t("add_new_user"))+" \n                        ")],1)],1),a("div",{staticClass:"col-md-auto col-12 "},[a("q-input",{attrs:{debounce:"1000",outlined:"",dense:"",placeholder:t.$t("search")},scopedSlots:t._u([{key:"append",fn:function(){return[a("q-icon",{attrs:{name:"search"}})]},proxy:!0}],null,!1,4009527860),model:{value:t.searchText,callback:function(e){t.searchText=e},expression:"searchText"}})],1)])])])]:t._e(),a("div",{},[a("div",{staticClass:"container-fluid"},[a("div",{staticClass:"row q-col-gutter-md"},[a("div",{staticClass:"col comp-grid"},[a("div",[t.showBreadcrumbs?[t.searchText||t.fieldName?a("q-breadcrumbs",{staticClass:"q-pa-md"},[t.fieldName?[t.$route.query.tag?a("q-breadcrumbs-el",{staticClass:"text-capitalize",attrs:{icon:"arrow_back",label:t.$route.query.tag,to:"/user"}}):a("q-breadcrumbs-el",{staticClass:"text-capitalize",attrs:{icon:"arrow_back",label:t._f("readable")(t.fieldName),to:"/user"}}),t.$route.query.label?a("q-breadcrumbs-el",{attrs:{label:t.$route.query.label}}):a("q-breadcrumbs-el",{attrs:{label:t.fieldValue}})]:t._e(),t.searchText?[a("q-breadcrumbs-el",{attrs:{icon:"search",label:t.$t("search")}}),a("span",{staticClass:"text-caption text-bold"},[a("q-chip",{attrs:{square:"",removable:""},on:{remove:function(e){t.searchText="",t.$route.query.search=""}}},[t._v(t._s(t.searchText))])],1)]:t._e()],2):t._e()]:t._e(),a("div",{staticClass:"relative-position"},[a("q-table",{attrs:{grid:t.$q.screen.lt.md,flat:t.$q.screen.gt.md,"table-header-class":"text-h4 ",bordered:!1,columns:t.$menus.UserTableHeaderItems,data:t.records,"binary-state-sort":"",separator:"horizontal",dense:!0,selected:t.selectedItems,selection:"multiple","row-key":"id",pagination:t.pagination,"hide-bottom":"","no-data-label":t.$t("no_record_found"),loading:t.loading},on:{"update:selected":function(e){t.selectedItems=e},"update:pagination":function(e){t.pagination=e},request:t.setPagination},scopedSlots:t._u([{key:"body",fn:function(e){return[a("q-tr",{attrs:{props:e}},[a("q-td",{attrs:{"auto-width":""}},[a("q-checkbox",{model:{value:e.selected,callback:function(a){t.$set(e,"selected",a)},expression:"props.selected"}})],1),a("q-td",{key:"id",attrs:{props:e}},[a("q-btn",{attrs:{padding:"xs",rounded:!1,color:"primary","no-caps":"",unelevated:"",flat:"",to:"/user/view/"+e.row.id}},[t._v(t._s(e.row.id))])],1),a("q-td",{key:"name",attrs:{props:e}},[t._v("\n                                        "+t._s(e.row.name)+"\n                                    ")]),a("q-td",{key:"email",attrs:{props:e}},[a("q-btn",{attrs:{padding:"xs",flat:"",rounded:!1,size:"",color:"primary","no-caps":"",unelevated:"",type:"a",href:"mailto:"+e.row.email}},[t._v(t._s(e.row.email))])],1),a("q-td",{key:"btnactions",attrs:{props:e}},[a("q-btn",{attrs:{icon:"visibility",rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",title:t.$t("view_record"),to:"/user/view/"+e.row.id}}),a("q-btn",{staticClass:"q-mx-xs",attrs:{icon:"edit",rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",title:t.$t("edit_this_record"),to:"/user/edit/"+e.row.id}}),a("q-btn",{attrs:{rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",icon:"clear",title:t.$t("delete_this_record")},on:{click:function(a){return t.deleteItem(e.row.id)}}})],1)],1)]}},{key:"item",fn:function(e){return[a("div",{staticClass:"q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition",style:e.selected?"transform: scale(0.95);":""},[a("q-card",{class:e.selected?"bg-grey-2":"",attrs:{bordered:"",flat:""}},[a("div",[a("q-checkbox",{model:{value:e.selected,callback:function(a){t.$set(e,"selected",a)},expression:"props.selected"}})],1),a("q-separator"),a("q-card-section",[a("div",{staticClass:"row q-py-sm q-col-gutter-md justify-content-between"},[a("div",{staticClass:"col-auto text-weight-light text-caption"},[t._v("\n                                                "+t._s(t.$t("id"))+"\n                                            ")]),a("div",{staticClass:"col text-weight-bold text-right"},[a("q-btn",{attrs:{padding:"xs",rounded:!1,color:"primary","no-caps":"",unelevated:"",flat:"",to:"/user/view/"+e.row.id}},[t._v(t._s(e.row.id))])],1)]),a("div",{staticClass:"row q-py-sm q-col-gutter-md justify-content-between"},[a("div",{staticClass:"col-auto text-weight-light text-caption"},[t._v("\n                                                "+t._s(t.$t("name"))+"\n                                            ")]),a("div",{staticClass:"col text-weight-bold text-right"},[t._v("\n                                                "+t._s(e.row.name)+"\n                                            ")])]),a("div",{staticClass:"row q-py-sm q-col-gutter-md justify-content-between"},[a("div",{staticClass:"col-auto text-weight-light text-caption"},[t._v("\n                                                "+t._s(t.$t("email"))+"\n                                            ")]),a("div",{staticClass:"col text-weight-bold text-right"},[a("q-btn",{attrs:{padding:"xs",flat:"",rounded:!1,size:"",color:"primary","no-caps":"",unelevated:"",type:"a",href:"mailto:"+e.row.email}},[t._v(t._s(e.row.email))])],1)])]),a("q-separator"),a("q-card-actions",[a("q-btn",{attrs:{icon:"visibility",rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",title:t.$t("view_record"),to:"/user/view/"+e.row.id}}),a("q-btn",{staticClass:"q-mx-xs",attrs:{icon:"edit",rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",title:t.$t("edit_this_record"),to:"/user/edit/"+e.row.id}}),a("q-btn",{attrs:{rounded:!1,"no-caps":"",unelevated:"",size:"sm",padding:"xs",color:"accent",icon:"clear",title:t.$t("delete_this_record")},on:{click:function(a){return t.deleteItem(e.row.id)}}})],1)],1)],1)]}}])}),a("q-inner-loading",{attrs:{showing:t.loading}},[a("q-spinner",{attrs:{color:"",size:"20px"}})],1),t.showFooter?a("div",{},[a("div",{directives:[{name:"show",rawName:"v-show",value:!t.loading,expression:"!loading"}],staticClass:"q-pa-sm q-my-md"},[a("div",{staticClass:"row justify-between"},[a("div",{staticClass:"row q-col-gutter-md"},[a("div",[t.selectedItems.length?a("q-btn",{staticClass:"q-mx-xs",attrs:{"display-style":"modal",rounded:!1,"no-caps":"",unelevated:"",color:"negative",padding:"xs",icon:"delete_sweep",title:t.$t("delete_selected")},on:{click:function(e){return t.deleteItem(t.selectedItems)}}}):t._e()],1)]),t.paginate&&t.totalRecords>0?a("div",{staticClass:"row q-col-gutter-md justify-center"},[t.totalPages>1?a("div",{staticClass:"col-auto"},[a("q-chip",[t._v(t._s(t.$t("records"))+" "+t._s(t.recordsPosition)+" "+t._s(t.$t("of"))+" "+t._s(t.totalRecords))])],1):t._e(),t.totalPages>1?a("div",{staticClass:"col-auto"},[a("q-chip",[t._v(t._s(t.$t("page"))+" "+t._s(t.pagination.page)+" "+t._s(t.$t("of"))+"  "+t._s(t.totalPages))])],1):t._e(),a("div",{staticClass:"col-auto"},[a("q-select",{attrs:{dense:!0,"options-dense":"",outlined:"","emit-value":"",options:[5,10,15,20,30,40,50,100,200]},model:{value:t.pagination.rowsPerPage,callback:function(e){t.$set(t.pagination,"rowsPerPage",e)},expression:"pagination.rowsPerPage"}})],1),t.totalPages>1?a("div",[a("q-pagination",{attrs:{"direction-links":!0,"boundary-links":!0,"max-pages":5,"boundary-numbers":!0,max:t.totalPages},model:{value:t.pagination.page,callback:function(e){t.$set(t.pagination,"page",e)},expression:"pagination.page"}})],1):t._e()]):t._e()])])]):t._e()],1)],2)])])])])],2)},i=[],o=a("ded3"),r=a.n(o),n=a("c6e7"),d=a("c770"),l=a("2f62"),c={name:"listUserPage",components:{},mixins:[n["a"],d["a"]],props:{primaryKey:{type:String,default:"id"},pageName:{type:String,default:"user"},routeName:{type:String,default:"userlist"},apiPath:{type:String,default:"user/index"},msgBeforeDelete:{type:String,default:function(){return this.$t("are_you_sure_you_want_to_delete_this_record")}}},data(){return{}},computed:{pageTitle:{get:function(){return this.$t("user")}},records:{get:function(){return this.$store.getters["user/records"]},set:function(t){this.$store.commit("user/setRecords",t)}}},meta(){return{title:this.pageTitle}},watch:{apiUrl:function(){this.load()},$route(t,e){t.name==this.routeName&&this.load()}},methods:r()(r()({},Object(l["b"])("user",["fetchRecords","deleteRecord"])),{},{load:function(){if(!this.loading){this.loading=!0;let t=this.apiUrl,e={url:t,merge:!1};this.fetchRecords(e).then((t=>{this.loading=!1,this.ready=!0,this.totalRecords=t.total_records,this.recordCount=t.record_count,this.pagination.rowsNumber=this.totalRecords}),(t=>{this.loading=!1,this.showPageRequestError(t)}))}}})},u=c,p=a("2877"),m=a("f09f"),g=a("9c40"),b=a("0016"),v=a("27f9"),h=a("ead5"),_=a("079e"),q=a("b047"),f=a("eaac"),w=a("bd08"),x=a("db86"),y=a("8f8e"),C=a("eb85"),$=a("a370"),k=a("4b7e"),Q=a("74f7"),P=a("0d59"),z=a("ddd8"),T=a("3b16"),I=a("eebe"),S=a.n(I),R=Object(p["a"])(u,s,i,!1,null,null,null);e["default"]=R.exports;S()(R,"components",{QCard:m["a"],QBtn:g["a"],QIcon:b["a"],QInput:v["a"],QBreadcrumbs:h["a"],QBreadcrumbsEl:_["a"],QChip:q["a"],QTable:f["a"],QTr:w["a"],QTd:x["a"],QCheckbox:y["a"],QSeparator:C["a"],QCardSection:$["a"],QCardActions:k["a"],QInnerLoading:Q["a"],QSpinner:P["a"],QSelect:z["a"],QPagination:T["a"]})}}]);