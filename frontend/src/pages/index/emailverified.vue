<template>
    <div class="container">
        <div class="row justify-center">
            <div class="col-md-6">
                <q-card flat bordered class="q-my-lg text-center">
                    <q-card-section>
                        <div class="text-h5 text-bold text-positive">
                            <q-icon size="lg" name="check_circle"></q-icon>
							{{ $t('email_verification_completed') }}
                        </div>
                       <q-separator class="q-my-md" />
                        <q-btn to="/" flat color="info">{{ $t('continue') }}</q-btn>
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </div>
</template>
<script>
	export default {
		props: {},
		data: function () {
			return {
			};
		},
		methods: {},
	};
</script>