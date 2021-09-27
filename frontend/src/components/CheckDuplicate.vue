<template>
    <api-data-source :api-path="apiPath" v-slot="apiProp">
		<slot :loading="apiProp.loading" :check="check" :exist="checkExits(apiProp.response)"></slot>
	</api-data-source>                 
</template>
<script>
    export default {
        props: {
            checkPath: '',
            value: '',
        },
        data: function() {
            return {
                error: '',
				loading: false,
				apiPath: '',
            };
		},
        methods: {
            check(){
				let val = this.value;
				if(val){
					this.apiPath = this.checkPath  + this.value;
				}
            },
            checkExits(val){
                if(val === true){
                    return true;
                }
                return false;
            }
        },
    }
</script>
