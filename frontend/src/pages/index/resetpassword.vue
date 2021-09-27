<template>
	<div class="container">
        <div class="row justify-center">
            <div class="col col-md-4">
                <q-card  flat bordered class="q-my-lg">
                    <q-card-section>
                        <div class="q-my-md">
                            <div class="text-h5 text-bold">{{ $t('password_reset') }}</div>
                        </div>
                        <ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="resetPassword()">
							<div class="q-my-md">
								<ValidationProvider :rules="{required:true}" name="Password" v-slot="{ errors, invalid, validated }">
									<q-input
										v-model="formData.password"
										outlined
										dense
										:placeholder="$t('new_password')"
										type="password"
										:error="invalid && validated" :error-message="errors[0]"
									/>
									</ValidationProvider>
							</div>
							<div class="q-my-md">
								<ValidationProvider :rules="{required:true, is: formData.password}" name="Confirm Password" v-slot="{ errors, invalid, validated }">
									<q-input
										v-model="formData.confirm_password"
										outlined
										dense
										:placeholder="$t('change_password')"
										type="password"
										:error="invalid && validated" :error-message="errors[0]"
									/>
									</ValidationProvider>
							</div>
							<div class="col-md-3 col-sm-4">
								<q-btn  :disabled="invalid" color="primary" unelevated type="submit" :loading="saving">
									<q-spinner-oval slot="loading" /> {{ $t('change_password') }}
								</q-btn>
							</div>
                        </ValidationObserver>
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </div>
</template>
<script>
import { PageMixin } from "../../mixins/page.js";
export default {
	props: {},
	mixins: [PageMixin],
    data: function () {
        return {
            formData: {
				password: "",
				confirm_password: "",
				token: "",
				email: ""
			},
			saving:false,
        };
    },
    methods: {
        async resetPassword(){
			const isFormValid = await this.$refs.observer.validate();
			if(isFormValid){
				this.saving = true;
				this.formData.token = this.$route.query.token;
				this.formData.email = this.$route.query.email;
				this.$api.post("auth/resetpassword", this.formData).then((response) => {
					this.saving = false;
					this.$router.push("/index/resetpassword_completed");
				},
				(response) => {
					this.saving = false;
					this.showPageRequestError(response);
				});
			}
		},
    }
};
</script>