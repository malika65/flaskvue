<template>
    <div>
        <template v-if="showHeader">
            <q-card bordered  flat  class="q-pa-md q-mb-md no-border-radius ">
                <div class="container">
                    <div class="row justify-between q-col-gutter-md">
                        <div class="col ">
                            <div class="text-h6 text-bold record-title">{{ $t('add_new_user') }}</div>
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
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('password') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true}" :name="$t('password')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlpassword" v-model="formData.password"  :label="$t('password')" :type="isPwd ? 'password' : 'text'" :placeholder="$t('enter_password')"    
                                                    class="" :error="invalid && validated" :error-message="errors[0]">
                                                    <template v-slot:append>
                                                        <q-icon
                                                        :name="isPwd ? 'visibility_off' : 'visibility'"
                                                        class="cursor-pointer"
                                                        @click="isPwd = !isPwd"
                                                        />
                                                    </template>
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('confirm_password') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <ValidationProvider :rules="{required:true, is: formData.password}" :name="$t('confirm_password')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="" v-model="formData.confirm_password" type="password" :label="$t('confirm_password')" :placeholder="$t('confirm_password')" :error="invalid && validated" :error-message="errors[0]" >
                                                    <template v-slot:append>
                                                        <q-icon
                                                        :name="isPwd ? 'visibility_off' : 'visibility'"
                                                        class="cursor-pointer"
                                                        @click="isPwd = !isPwd"
                                                        />
                                                    </template>
                                                    </q-input>
                                                </ValidationProvider>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="">
                                        <div class="row">
                                            <div class="col-sm-3 col-12">
                                                {{ $t('email') }} *
                                            </div>
                                            <div class="col-sm-9 col-12">
                                                <check-duplicate v-model="formData.email" check-path="components_data/user_email_exist/" v-slot="checker">
                                                <ValidationProvider :rules="{required:true, email:true}" :name="$t('email')" v-slot="{ errors, invalid, validated }">
                                                    <q-input outlined dense  ref="ctrlemail" @blur="checker.check" :loading="checker.loading" v-model="formData.email"  :label="$t('email')" type="email" :placeholder="$t('enter_email')"    
                                                    class="" :error="(invalid && validated) || checker.exist" :error-message="errors[0] || $t('not_available')">
                                                    </q-input>
                                                </ValidationProvider>
                                                </check-duplicate>
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
		name: 'addUserPage',
		components: {
		},
		mixins: [PageMixin, AddPageMixin],
		props:{
			pageName : {
				type : String,
				default : 'user',
			},
			routeName : {
				type : String,
				default : 'useradd',
			},
			apiPath : {
				type : String,
				default : 'user/add',
			},
		},
		data() {
            return {
				formData: {
					name: "", password: "", confirm_password: "", email: "", 
				},
			}
		},
		computed: {
			pageTitle:{
				get: function () {
					return this.$t('add_new_user')
				}
			}
		},
		meta () {
			return {
				title: this.pageTitle
			}
		},
		methods: {
			...mapActions('user', ['saveRecord']),
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
						this.navigateTo(`/user`);
					},
					 (response) => {
						this.saving = false;
						this.showPageRequestError(response);
					});
				}
			},
			resetForm (){
				this.formData = {name: "", password: "", confirm_password: "", email: "", };
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
