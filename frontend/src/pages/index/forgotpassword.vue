<template>
    <div class="container">
        <div class="row justify-center">
            <div class="col col-md-6">
                <q-card flat bordered class="q-my-lg">
                    <q-card-section>
                        <div class="q-my-md">
                            <div class="text-h5 text-bold">{{ $t('password_reset') }}</div>
                            <small class="text-caption">
                                {{ $t('please_provide_the_valid_email_address_you_used_to_register') }}
                            </small>
                        </div>
						<q-banner v-if="sentMsg" inline-actions rounded class="bg-green-1 q-my-lg">
							<template v-slot:avatar>
								<q-icon color="positive" name="email" />
							</template>
							<div class="text-bold">{{ sentMsg }}</div>
						</q-banner>
						 <ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="sendEmail()">
							<div class="row q-col-gutter-lg">
								<div class="col-md-9 col">
									<ValidationProvider :rules="{required:true, email: true}" name="Email" v-slot="{ errors, invalid, validated }">
									<q-input
										v-model="formData.email"
										outlined
										dense
										:placeholder="$t('email')"
										type="email"
										:error="invalid && validated" :error-message="errors[0]"
									/>
									</ValidationProvider>
								</div>
								<div class="col-md-3 col-sm-4">
									<q-btn  :disabled="invalid" color="primary" unelevated type="submit" :loading="saving">
										<q-spinner-oval slot="loading" /> 	{{ $t('send') }} <q-icon name="email"></q-icon>
									</q-btn>
								</div>
							</div>
						 </ValidationObserver>
                        <br />
                        <div class="text-info">
                            {{ $t('a_link_will_be_sent_to_your_email_containing_the_information_you_need_for_your_password') }}
                        </div>
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
				email: ""
			},
			saving:false,
			error:"",
			sentMsg:"",
        };
    },
    methods: {
		async sendEmail(){
			const isFormValid = await this.$refs.observer.validate();
			if(isFormValid){
				this.saving = true;
				this.$api.post("auth/forgotpassword", this.formData).then( (response) => {
					this.saving = false;
					this.sentMsg = response.data;
				},
				(response) => {
					this.saving = false;
					this.showPageRequestError(response);
					this.sentMsg = "";
				});
			}
		},
	},
};
</script>