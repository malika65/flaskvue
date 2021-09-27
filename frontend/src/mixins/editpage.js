export const EditPageMixin = {
	props: {
		id : {
			type : String,
			default : '',
		},
		msgAfterUpdate : {
			type : String,
			default : function(){ return this.$t('record_updated_successfully'); },
		},

		showHeader : {
			type : Boolean,
			default : true,
		},
		showSubmitButton: {
			type : Boolean,
			default : true,
		},
		modelBind: {
			type: Object,
			default: function () { return {} }
		}
	},
	data: function() {
		return {
			inputSearch : "",
			errorMsg : "",
			loading : false,
			ready: false,
			saving : false,
		}
	},
	computed: {
		apiUrl: function() {
			return this.apiPath + "/" + this.id;
		},
	},
	methods: {
		async submit(){
			const isFormValid = await this.$refs.observer.validate();
			if(isFormValid){
				this.saving = true;
				let payload = this.formData;
				let url = this.apiUrl;
				let data = {url, payload}
				this.saveRecord(data).then((response) => {
					this.id = response.data
					this.saving = false;
					this.closeDialogs();// close page dialog that if opened
					this.$emit("submited", this.id);
				},
				 (response) => {
					this.saving = false;
					this.$emit("error", response);
				});
			}
		},
		load: function(){
			var url = this.apiUrl;
			this.loading = true;
			this.$api.get(url).then((response) => {
					this.loading = false
					this.ready = true
					this.formData = response.data;
					this.updateFormFields();
				},
				 (response) => {
					 this.resetForm();
					this.loading = false;
					this.showPageRequestError(response);
				}
			);
		},
	},
	watch: {
		$route (to, from){
			//only fetch data when navigated to this page
			if(to.name == this.routeName){
				this.load();
			}
		},
		modelBind: function(){
			for(key in this.modelBind){
				this.formData[key]= this.modelBind[key];
			}
		}
	},
	mounted: function() {
		this.load();
	},
}