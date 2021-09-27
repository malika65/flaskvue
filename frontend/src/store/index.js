import Vue from 'vue'
import Vuex from 'vuex'
import { pageComponents } from "./page_components.js"
import { auth } from "./auth.js"
import { user } from "./user.js"
import { blacklist } from "./blacklist.js"
Vue.use(Vuex)
export default function (/* { ssrContext } */) {
	const Store = new Vuex.Store({
		modules: {
			pageComponents,
			auth,
		user,
		blacklist
		},
		// enable strict mode (adds overhead!)
		// for dev mode only
		strict: process.env.DEV
	})
	return Store
}