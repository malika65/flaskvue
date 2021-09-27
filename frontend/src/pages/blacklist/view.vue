<template>
    <div>
        <template v-if="showHeader">
            <q-card bordered  flat  class="q-pa-md q-mb-md no-border-radius ">
                <div class="container">
                    <div class="row justify-between q-col-gutter-md">
                        <div class="col ">
                            <div class="text-h6 text-bold record-title">{{ $t('view_blacklist') }}</div>
                        </div>
                    </div>
                </div>
            </q-card>
        </template>
        <div class="">
            <div class="container">
                <div class="row q-col-gutter-md">
                    <div class="col comp-grid">
                        <q-card bordered  flat  class=" ">
                            <div>
                                <div v-if="!loading">
                                    <div v-if="item" class="page-records ">
                                        <q-list clickable>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('id') }}: </q-item-label>
                                                    <q-item-label>{{ item.id }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('name') }}: </q-item-label>
                                                    <q-item-label>{{ item.name }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('organization') }}: </q-item-label>
                                                    <q-item-label>{{ item.organization }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('description') }}: </q-item-label>
                                                    <q-item-label>{{ item.description }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('sum') }}: </q-item-label>
                                                    <q-item-label>{{ item.sum }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('reiting') }}: </q-item-label>
                                                    <q-item-label>{{ item.reiting }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                        </q-list>
                                        <div class="q-pa-sm">
                                            <q-btn    :rounded="false"  no-caps  unelevated   size="sm" padding="xs" color="accent" icon="edit"  class="q-mx-xs" :title="$t('edit_this_record')"  :to="`/blacklist/edit/${item.id }`">
                                            </q-btn>
                                            <q-btn    :rounded="false"  no-caps  unelevated   size="sm" padding="xs" color="accent" icon="clear" class="q-mx-xs" @click="deleteItem(item.id)" :title="$t('delete_this_record')">
                                            </q-btn>
                                        </div>
                                    </div>
                                    <!--<div class="q-pa-sm" v-else>
                                        <q-icon name="block"></q-icon> {{ $t('no_record_found') }}
                                    </div>-->
                                </div>
                                <div v-else class="q-pa-sm text-center">
                                    <q-spinner
                                    :size="40"
                                    color="accent"
                                    indeterminate>
                                    </q-spinner>
                                    Loading...
                                </div>
                            </div>
                        </q-card>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
	import { PageMixin } from "../../mixins/page.js";
	import { ViewPageMixin } from "../../mixins/viewpage.js";
	import { mapActions, mapGetters, mapState } from "vuex";
	export default {
		name: 'viewBlacklistPage',
		components: {
		},
		mixins: [PageMixin, ViewPageMixin],
		props: {
			pageName: {
				type : String,
				default : 'blacklist',
			},
			routeName : {
				type : String,
				default : 'blacklistview',
			},
			apiPath: {
				type : String,
				default : 'blacklist/view',
			},
		},
		data() {
            return {
				item: {
					default :{
					},
				},
			}
		},
		computed: {
			pageTitle:{
				get: function () {
					return this.$t('view_blacklist')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle
			}
		},
		methods: {
			...mapActions("blacklist", [ "fetchRecord", "deleteRecord"]),
		},
		watch: {
			$route (to, from){
				//only fetch data when navigated to this page
				if(to.name == this.routeName){
					this.load();
				}
			},
		},
	};
	</script>
