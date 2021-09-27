<template>
    <div>
        <template v-if="showHeader">
            <q-card bordered  flat  class="q-pa-md q-mb-md no-border-radius ">
                <div class="container">
                    <div class="row justify-between q-col-gutter-md">
                        <div class="col ">
                            <div class="text-h6 text-bold record-title">{{ $t('add_new_blacklist') }}</div>
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
                                <ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="startSaveRecord()" @reset="resetForm">
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('name') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('name')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlname" v-model="formData.name"  :label="$t('name')" type="text" :placeholder="$t('enter_name')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('organization') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('organization')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlorganization" v-model="formData.organization"  :label="$t('organization')" type="text" :placeholder="$t('enter_organization')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('description') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('description')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrldescription" v-model="formData.description"  :label="$t('description')" type="text" :placeholder="$t('enter_description')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('sum') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('sum')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlsum" v-model="formData.sum"  :label="$t('sum')" type="text" :placeholder="$t('enter_sum')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('reiting') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('reiting')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlreiting" v-model="formData.reiting"  :label="$t('reiting')" type="text" :placeholder="$t('enter_reiting')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div v-if="showSubmitButton" class="text-center q-my-md">
                                        <q-btn type="submit"    :rounded="false"  color="primary"  no-caps  unelevated   :disabled="invalid" icon="send" :loading="saving">
                                            <q-spinner-oval slot="loading" /> {{ $t('submit') }}
                                        </q-btn>
                                    </div>
                                </ValidationObserver>
                                <slot :submit="submit" :saving="saving"></slot>
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
	import { AddPageMixin } from "../../mixins/addpage.js";
	import { mapActions } from "vuex";
	export default {
		name: 'addBlacklistPage',
		components: {
		},
		mixins: [PageMixin, AddPageMixin],
		props:{
			pageName : {
				type : String,
				default : 'blacklist',
			},
			routeName : {
				type : String,
				default : 'blacklistadd',
			},
			apiPath : {
				type : String,
				default : 'blacklist/add',
			},
		},
		data() {
            return {
				formData: {
					name: "", organization: "", description: "", sum: "", reiting: "", 
				},
			}
		},
		computed: {
			pageTitle:{
				get: function () {
					return this.$t('add_new_blacklist')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle
			}
		},
		methods: {
			...mapActions('blacklist', ['saveRecord']),
			async startSaveRecord(){
				const isFormValid = await this.$refs.observer.validate();
				if(isFormValid){
					this.saving = true;
					let payload = this.normalizedFormData();
					let url = this.apiUrl;
					let data = { url, payload  }
					this.saveRecord(data).then((response) => {
						this.record = response.data;
						this.id = this.record['id'];
						this.saving = false;
						this.resetForm();
						this.closeDialogs();// close page dialog that if opened
						this.flashMsg(this.msgAfterSave);
						this.navigateTo(`/blacklist`);
					},
					 (response) => {
						this.saving = false;
						this.showPageRequestError(response);
					});
				}
			},
			resetForm (){
				this.formData = {name: "", organization: "", description: "", sum: "", reiting: "", };
				requestAnimationFrame(() => {
					this.$refs.observer.reset();
				});
				this.$EventBus.$emit("resetForm");
			},
		},
		mounted : function() {
		},
	};
	</script>
