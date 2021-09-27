<template>
    <div>
        <div class="">
            <div class="container">
                <div class="row q-col-gutter-md">
                    <div class="col comp-grid">
                        <div>
                            <div v-if="!loading">
                                <div class="bg-primary text-white q-pa-lg q-my-md">
                                    <div class="row q-col-gutter-lg">
                                        <div class="col-auto">
                                            <q-icon
                                            size="50px"
                                            color="white"
                                            name="account_box"
                                            ></q-icon>
                                        </div>
                                        <div class="col">
                                            <div class="text-h4 text-white text-weight-bold"> {{ $UserName }} </div>
                                            <div class="text-capitalize">  </div>
                                            <!--<div class="text-subtitle2">{{ $UserEmail }}</div>-->
                                        </div>
                                    </div>
                                </div>
                                <div class="row q-col-gutter-md">
                                    <div class="col-md-3 col-sm-3 col-12">
                                        <q-card  bordered  flat  class=" q-pa-sm">
                                            <q-tabs vertical class="text-primary" v-model="tab" no-caps inline-label>
                                            <q-tab name="accountview" icon="account_box" :label="$t('account_detail')" />
                                            <q-tab name="accountedit" icon="edit" :label="$t('edit_account')" />
                                            <q-tab name="changepassword" icon="lock" :label="$t('change_password')" />
                                            </q-tabs>
                                        </q-card>
                                    </div>
                                    <div class="col-md-9 col-sm-9 col-12">
                                        <q-tab-panels v-model="tab" animated transition-prev="jump-up" transition-next="jump-up">
                                        <q-tab-panel name="accountview">
                                        <div v-if="!loading && ready">
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('name') }}: </q-item-label>
                                                    <q-item-label>{{ item.name }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                            <q-separator></q-separator>
                                            <q-item clickable v-ripple>
                                                <q-item-section>
                                                    <q-item-label caption>{{ $t('id') }}: </q-item-label>
                                                    <q-item-label>{{ item.id }}</q-item-label>
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
                                        </div>
                                        <div v-if="loading" class="q-pa-sm text-center">
                                            <q-spinner :size="40" color="accent" indeterminate></q-spinner>
                                            Loading...
                                        </div>
                                        </q-tab-panel>
                                        <q-tab-panel name="accountedit">
                                        <div class="reset-grid">
                                            <account-edit-page></account-edit-page>
                                        </div>
                                        </q-tab-panel>
                                        <q-tab-panel name="changepassword">
                                        <change-password-page></change-password-page>
                                        </q-tab-panel>
                                        </q-tab-panels>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="q-pa-lg text-center">
                                <q-spinner :size="50" color="accent" indeterminate></q-spinner>
                                {{ $t('loading') }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
	import { PageMixin } from "../../mixins/page.js";
	import { ViewPageMixin } from "../../mixins/viewpage.js";
	import  AccountEditPage  from "./accountedit.vue";
	import  ChangePasswordPage  from "./changepassword.vue";
	export default {
		name: 'accountviewUserPage',
		components: {
			AccountEditPage,
			ChangePasswordPage,
		},
		mixins: [PageMixin, ViewPageMixin],
		props: {
			pageName: {
				type : String,
				default : 'user',
			},
			routeName : {
				type : String,
				default : 'useraccountview',
			},
			apiPath: {
				type : String,
				default : 'account',
			},
		},
		data() {
            return {
				item: {
					default :{
					},
				},
				tab: 'accountview',
			}
		},
		computed: {
			pageTitle:{
				get: function () {
					return this.$t('my_account')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle
			}
		},
		methods: {
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
