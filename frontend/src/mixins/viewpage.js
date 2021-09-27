export const ViewPageMixin = {
	props: {
		id : {
			type : String,
			default : '',
		},
		fieldName : {
			type : String,
			default : '',
		},
		fieldValue : {
			type : String,
			default : '',
		},
		editButton : {
			type : Boolean,
			default : true,
		},
		deleteButton : {
			type : Boolean,
			default : true,
		},
		exportButton : {
			type : Boolean,
			default : true,
		},
		msgBeforeDelete : {
			type : String,
			default : function(){ return this.$t('are_you_sure_you_want_to_delete_this_record'); },
		},
		msgAfterDelete : {
			type : String,
			default : function(){ return this.$t('record_deleted_successfully'); },
		},
		showHeader : {
			type : Boolean,
			default : true,
		},
		showFooter: {
			type : Boolean,
			default : true,
		},
	},
	data : function() {
		return {
			filterBy : '',
			filterValue : '',
			ready : false,
			loading : false,
			showError: false,
			errorMsg : '',
			
		}
	},
	computed: {
		apiUrl: function() {
			return this.apiPath + '/' + this.id;
		},
	},
	methods :{
		load : function(){
			if (!this.loading) {
				this.loading = true;
				this.item = null;
				let url = this.apiUrl;
				this.$api.get(url).then(
				  response => {
					this.loading = false;
					this.ready = true;
					this.item = response.data
				  },
				  response => {
					this.loading = false;
					this.showPageRequestError(response);
				  }
				);
			}
		},
		deleteItem: function (id) {
			if (id) {
				let title = this.$t('delete_record');
				let prompt = this.msgBeforeDelete;
				this.$q.dialog({
					title: title,
					message: prompt,
					cancel: true,
					persistent: true
				}).onOk(() => {
					let url = this.pageName + '/delete/' + id
					let data =  {id, url};
					this.deleteRecord(data).then(
						(response) => {
							this.flashMsg(this.msgAfterDelete);
							this.$router.back();
						},
						(response) => {
							this.showPageRequestError(response);
						});
				}).onCancel(() => {
					// console.log('>>>> Cancel')
				}).onDismiss(() => {
					// console.log('I am triggered on both OK and Cancel')
				})
			}
		},
		exportRecord : function(){
			this.exportPage(this.$refs.datatable.innerHTML, this.pageTitle);
		}
	},
	watch: {
		apiUrl: function () {
			this.load();
		},
	},
	created: function(){
	
	},
	mounted: function() {
		this.filterBy = this.fieldName;
		this.filterValue = this.fieldValue;
		this.load();
		document.body.scrollTop = document.documentElement.scrollTop = 0;
	},
}