<template>
    <div>
        <template v-if="showHeader">
            <q-card bordered  flat  class="q-pa-md q-mb-md no-border-radius ">
                <div class="container">
                    <div class="row justify-between q-col-gutter-md">
                        <div class="col ">
                            <div class="text-h6 text-bold record-title">{{ $t('edit_user') }}</div>
                        </div>
                    </div>
                </div>
            </q-card>
        </template>
        <div class="">
            <div class="container">
                <div class="row q-col-gutter-md">
                    <div class="col-md-9 col-12 comp-grid">
                        <q-card bordered  flat  class="q-pa-md ">
                            <div>
                                <div v-if="!loading">
                                    <ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="startRecordUpdate()">
                                        <div class="">
                                            <div class="row">
                                                <div class="col-sm-3 col-12">
                                                    {{ $t('name') }} *
                                                </div>
                                                <div class="col-sm-9 col-12">
                                                    <check-duplicate v-model="formData.name" check-path="components_data/user_name_exist/" v-slot="checker">
                                                    <ValidationProvider :rules="{required:true}" :name="$t('name')" v-slot="{ errors, invalid, validated }">
                                                        <q-input outlined dense  ref="ctrlname" @blur="checker.check" :loading="checker.loading" v-model="formData.name"  :label="$t('name')" type="text" :placeholder="$t('enter_name')"    
                                                        class="" :error="(invalid && validated) || checker.exist" :error-message="errors[0] || $t('not_available')">
                                                        </q-input>
                                                    </ValidationProvider>
                                                    </check-duplicate>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-if="showSubmitButton" class="text-center q-my-md">
                                            <q-btn    :rounded="false"  color="primary"  no-caps  unelevated   type="submit" :disabled="invalid" icon="send" :loading="saving">
                                                <q-spinner-oval slot="loading" /> {{ $t('update') }}
                                            </q-btn>
                                        </div>
                                    </ValidationObserver>
                                    <slot :submit="submit" :saving="saving"></slot>
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
	import { EditPageMixin } from "../../mixins/editpage.js";
	import { mapActions } from "vuex";
	export default {
		name: 'editUserPage',
		components: {
		},
		mixins: [PageMixin, EditPageMixin],
		props: {
			pageName: {
				type: String,
				default: 'user',
			},
			routeName: {
				type: String,
				default: 'useredit',
			},
			apiPath: {
				type: String,
				default: 'user/edit',
			},
		},
		data() {
            return {
				formData: {
					name: "", 
				},
        	}
		},
		computed: {
			pageTitle:{
				get: function () {
					return this.$t('edit_user')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle // set browser page title
			}
		},
		methods: {
			...mapActions('user', ['updateRecord', 'fetchRecord']),
			async startRecordUpdate(){
				const isFormValid = await this.$refs.observer.validate();
				if(isFormValid){
					this.saving = true;
					let id = this.id;
					let url = this.apiUrl;
					let payload = this.normalizedFormData();
					let data = { id, url, payload }
					this.updateRecord(data).then(
						(response) => {
							this.saving = false;
							this.flashMsg(this.msgAfterUpdate);
							this.resetForm();
							this.closeDialogs();// close page dialog that if opened
							this.navigateTo(`/user`);
						},
						(response) => {
							this.saving = false;
							this.showPageRequestError(response);
						}
					);
				}
			},
			updateFormFields: function(){
				//update form fields value after load from api
				//e.g convert fieldvalue (value,value2,value2) to array 
            },
			resetForm (){
				//reset form fields value
				this.formData = {name: "", };
				requestAnimationFrame(() => {
					this.$refs.observer.reset();
				});
				//raise event to reset other custom form components
				this.$EventBus.$emit("resetForm");
			},
		},
	};
	</script>
