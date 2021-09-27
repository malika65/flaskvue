
import { ApiService } from '../services/api'
import { StorageService } from '../services/storage'
export const auth = {
	namespaced: true,
	state: {
		user: null,
		userPages: [],
		userRoles: [],
	},
	getters: {
		getLoginToken(state) {
			let token = StorageService.getToken() || null;
			return token;
		}
	},
	mutations: {
		setUserData(state, user) {
			state.user = user
		},
	},
	actions: {
		getUserData: async ({ commit }, payload) => {
			return new Promise((resolve, reject) => {
				ApiService.get("account/currentuserdata")
					.then(resp => {
						let data = resp.data;
						commit("setUserData", data);
						resolve(data);
					})
					.catch(err => {
						reject(err)
					})
			})
		},
		login: ({ commit }, payload) => {
			return new Promise((resolve, reject) => {
				ApiService.post("auth/login", payload.formData)
					.then(resp => {
						let loginData = resp.data;
						if(loginData.user && loginData.token){
							StorageService.saveLoginData(loginData, payload.rememberUser);
						}
						resolve(resp);
					})
					.catch(err => {
						reject(err);
					})
			})
		},
		logout: ({ commit }) => {
			// Remove the token and remove Authorization header from Api Service as well 
			StorageService.removeLoginData();
			ApiService.removeHeader();
		},
	}
}
