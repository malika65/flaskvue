
	
<template>
	<div class="container">
		<div class="row">
			<div class="col-md-5 col-12">
				<div class="text-h5 text-bold q-my-md">{{ $t('change_password') }}</div>
				<ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="startSaveRecord()">
					<ValidationProvider :rules="{required:true}" :name="$t('current_password')" v-slot="{ errors, invalid, validated }">
						<q-input 
							outlined dense 
							:label="$t('current_password')" 
							:placeholder="$t('current_password')" 
							v-model="formData.oldpassword" 
							type="password" 
							:error="invalid && validated" 
							:error-message="errors[0]" />
					</ValidationProvider>
					<ValidationProvider :rules="{required:true}" :name="$t('new_password')" v-slot="{ errors, invalid, validated }">
						<q-input 
							outlined dense 
							:label="$t('new_password')" 
							:placeholder="$t('new_password')" 
							v-model="formData.newpassword"
							type="password" 
							:error="invalid && validated" 
							:error-message="errors[0]" />
					</ValidationProvider>
					<ValidationProvider :rules="{required:true, is: formData.newpassword}" :name="$t('confirm_new_password')" v-slot="{ errors, invalid, validated }">
						<q-input 
							outlined dense 
							:label="$t('confirm_new_password')" 
							:placeholder="$t('confirm_new_password')"
							v-model="formData.confirmpassword" 
							type="password" 
							:error="invalid && validated" 
							:error-message="errors[0]" />
					</ValidationProvider>
					<div class="q-mt-md text-center">
						<q-btn :disabled="invalid" unelevated type="submit" icon="send" color="primary" large :loading="saving">
							<q-spinner-oval slot="loading" /> {{ $t('change_password') }}
						</q-btn>
					</div>
				</ValidationObserver>
			</div>
		</div>
	</div>
</template>

<script>
import { PageMixin } from "../../mixins/page.js";
export default {
	props:{
		apiUrl: {
			type: String,
			default: 'account/changepassword'
		},
	},
	mixins: [PageMixin],
	data() {
		return {
			saving: false,
			formData: {
				oldpassword: '', 
				newpassword: '', 
				confirmpassword: '', 
			},
		}
	},
	methods: {
		async startSaveRecord(){
			const isFormValid = await this.$refs.observer.validate();
			if(isFormValid){
				this.saving = true;
				let payload = this.formData;
				let url = this.apiUrl;
				this.$api.post(url, payload).then((response) => {
					this.saving = false;
					this.resetForm();
					this.flashMsg("Password change completed");
				},(response) => {
					this.saving = false;
					this.showPageRequestError(response);
				});
			}
		},
		resetForm (){
			this.formData = {oldpassword: "", newpassword: "", confirmpassword: "", };
			requestAnimationFrame(() => {
				this.$refs.observer.reset();
			});
		},
	},
}
</script>

