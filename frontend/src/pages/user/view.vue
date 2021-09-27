<template>
    <div>
        <template v-if="showHeader">
            <q-card bordered  flat  class="q-pa-md q-mb-md no-border-radius ">
                <div class="container">
                    <div class="row justify-between q-col-gutter-md">
                        <div class="col ">
                            <div class="text-h6 text-bold record-title">{{ $t('view_user') }}</div>
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
                                <div class="bg-primary text-white q-pa-lg q-my-md">
                                    <div class="row q-col-gutter-lg">
                                        <div class="col-auto">
                                            <q-avatar font-size="48px" icon="account_circle"></q-avatar>
                                        </div>
                                        <div class="col">
                                            <div class="text-h4 text-weight-bold"> {{ item.name }}</div>
                                            <!--<div class="text-subtitle2">{{ item.email }}</div>-->
                                        </div>
                                    </div>
                                </div>
                                <div v-if="!loading">
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
                                            <q-item-label caption>{{ $t('email') }}: </q-item-label>
                                            <q-item-label>{{ item.email }}</q-item-label>
                                        </q-item-section>
                                    </q-item>
                                    <q-separator></q-separator>
                                    <div class="q-pa-md">
                                        <q-btn    :rounded="false"  no-caps  unelevated   size="sm" padding="xs" color="accent" icon="edit"  class="q-mx-xs" :title="$t('edit_this_record')"  :to="`/user/edit/${item.id }`">
                                        </q-btn>
                                        <q-btn    :rounded="false"  no-caps  unelevated   size="sm" padding="xs" color="accent" icon="clear" class="q-mx-xs" @click="deleteItem(item.id)" :title="$t('delete_this_record')">
                                        </q-btn>
                                    </div>
                                </div>
                                <div v-else class="q-pa-sm text-center">
                                    <q-spinner :size="40" color="primary" indeterminate></q-spinner>
                                    {{ $t('loading') }}
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
		name: 'viewUserPage',
		components: {
		},
		mixins: [PageMixin, ViewPageMixin],
		props: {
			pageName: {
				type : String,
				default : 'user',
			},
			routeName : {
				type : String,
				default : 'userview',
			},
			apiPath: {
				type : String,
				default : 'user/view',
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
					return this.$t('view_user')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle
			}
		},
		methods: {
			...mapActions("user", [ "fetchRecord", "deleteRecord"]),
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
