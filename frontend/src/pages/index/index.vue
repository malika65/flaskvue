        <template>
            <q-page padding>
                <div class="">
                    <div class="container">
                        <div class="row q-col-gutter-md">
                            <div class="col-sm-8 col-md-8 col-12 comp-grid">
                                <div class="">
                                    <div class="text-bold q-pa-lg text-h4">Add content here</div>
                                </div>
                            </div>
                            <div class="col-sm-4 col-md-4 col-12 comp-grid">
                                <q-card bordered  flat  class="q-pa-md q-mt-lg ">
                                    <div>
                                        <div class="text-h5 text-bold q-mb-lg">{{ $t('user_login') }}</div>
                                        <ValidationObserver ref="observer" v-slot="{ invalid }" tag="form" @submit.prevent="startLogin()" @reset="resetForm">
                                            <q-input class="q-mb-md" :label="$t('username_or_email')" outlined dense :placeholder="$t('username_or_email')" v-model="user.username"  required="required" type="text" >
                                            <template v-slot:prepend>
                                                <q-icon name="account_circle"></q-icon>
                                            </template>
                                            </q-input>
                                            <q-input :label="$t('password')"  class="q-mb-md" outlined dense :placeholder="$t('password')" required="required" v-model="user.password" type="password">
                                            <template v-slot:prepend>
                                                <q-icon name="lock"></q-icon>
                                            </template>
                                            </q-input>
                                            <div class="row q-mb-md">
                                                <div class="col-6">
                                                    <q-checkbox v-model="rememberUser"> {{ $t('remember_me') }}</q-checkbox>
                                                </div>
                                                <div class="col-6">
                                                    <q-btn to="/index/forgotpassword" class="text-danger" flat no-caps color="negative"> {{ $t('reset_password') }}</q-btn>
                                                </div>
                                            </div>
                                            <transition appear enter-active-class="animated bounceIn" leave-active-class="animated fadeOut">
                                                <q-banner dense  inline-actions rounded  class="bg-red-2 q-my-md" v-if="errorMsg">
                                                    <template v-slot:avatar>
                                                        <q-icon color="red" name="error"></q-icon>
                                                    </template>
                                                    {{ errorMsg.toString() }}
                                                    <template v-slot:action>
                                                        <q-btn @click="errorMsg = ''" dense flat icon="close" />
                                                        </template>
                                                    </q-banner>
                                                    </transition>
                                                    <div class="text-center">
                                                        <q-btn unelevated :loading="loading" color="primary" no-caps :disabled="invalid" icon="lock_open" class="full-width"  type="submit"> 
                                                            {{ $t('login') }} 
                                                        </q-btn>
                                                    </div>
                                                    <q-separator class="q-my-md"></q-separator>
                                                    <div class="row q-my-sm">
                                                        <div class="col text-caption">
                                                            <div class=" text-caption q-pa-sm">{{ $t('dont_have_an_account') }}</div>
                                                        </div>
                                                        <div class="col-auto text-right">
                                                            <q-btn unelevated icon="account_box" no-caps color="positive" class="full-width" to="/index/register">{{ $t('register') }}
                                                            </q-btn>
                                                        </div>
                                                    </div>
                                                </ValidationObserver>
                                            </div>
                                        </q-card>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </q-page>
                </template>
                <script>
			import { mapActions } from "vuex";
			export default {
				name: 'IndexComponent',
				components: {
				},
				data: function() {
					return {
						user: {
							username: '',
							password:'',
						},
						rememberUser: false,
						loading: false,
						ready: false,
						errorMsg : '',
					}
				},
				methods: {
					...mapActions('auth', ['login']),
					startLogin (){
						this.loading = true;
						this.errorMsg = '';
						let formData = this.user;
						let rememberUser = this.rememberUser
						let payload = {
							formData,
							rememberUser	
						};
						this.login(payload).then((response) => {
							this.loading = false;
							let loginData = response.data;
							if (loginData.token) {
								window.location = "/";
							}
							else{
								this.$router.push(loginData.nextpage);
							}
						},
						 (request) => {
							this.loading = false;
							this.errorMsg = request.response.data || "Unable to login";
						});
					},
					resetForm (){
						this.user = {
							username: '',
							password:''
						};
						requestAnimationFrame(() => {
							this.$refs.observer.reset();
						});
					},
				},
				mounted:function(){
					this.ready = true;
				}
			};
		</script>
