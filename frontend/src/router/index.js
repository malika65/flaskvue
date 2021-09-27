import Vue from 'vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter)
let routes = [
	{
		name: 'main',
		path: '/',
		component: () => import('layouts/MainLayout.vue'),
		children: [
			
			{ path: '/user/', name: 'userlist', component: () => import('pages/user/list.vue'), props: true},
			{ path: '/user/(list|index)/:fieldName?/:fieldValue?', name: 'userlistfilter', component: () => import('pages/user/list.vue'), props: true},
			
	
			{ path: '/user/view/:id', name: 'userview', component: () => import('pages/user/view.vue'), props: true},
			{ path: '/index/register', name: 'useruserregister' , component: () => import('pages/index/userregister.vue'), props: true},
			{ path: '/account/edit', name: 'useraccountedit' , component: () => import('pages/account/accountedit.vue'), props: true},
			{ path: '/account', name: 'useraccountview' , component: () => import('pages/account/accountview.vue'), props: true},
			{ path: '/user/add', name: 'useradd' , component: () => import('pages/user/add.vue'), props: true},
			{ path: '/user/edit/:id' , name: 'useredit' , component: () => import('pages/user/edit.vue') , props: true},
			{ path: '/blacklist/', name: 'blacklistlist', component: () => import('pages/blacklist/list.vue'), props: true},
			{ path: '/blacklist/(list|index)/:fieldName?/:fieldValue?', name: 'blacklistlistfilter', component: () => import('pages/blacklist/list.vue'), props: true},
			
	
			{ path: '/blacklist/view/:id', name: 'blacklistview', component: () => import('pages/blacklist/view.vue'), props: true},
			{ path: '/blacklist/add', name: 'blacklistadd' , component: () => import('pages/blacklist/add.vue'), props: true},
			{ path: '/blacklist/edit/:id' , name: 'blacklistedit' , component: () => import('pages/blacklist/edit.vue') , props: true},

			
			{ path: '/index/forgotpassword', name: 'forgotpassword', component: () => import('pages/index/forgotpassword.vue'), props: true},
			{ path: '/index/resetpassword', name: 'resetpassword', component: () => import('pages/index/resetpassword.vue'), props: true},
			{ path: '/index/resetpassword_completed', name: 'resetpassword_completed', component: () => import('pages/index/resetpassword_completed.vue'), props: true},
	
			
			{ path: '/error/forbidden', component: () => import('pages/errors/forbidden.vue') },
			{ path: '/error/notfound', component: () => import('pages/errors/pagenotfound.vue') }
		]
	},
];


/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default async function ({ store, ssrContext }) {
	let mainRoute = routes.find(x => x.name = "main");

	
	let loginToken = store.getters["auth/getLoginToken"];
	if(loginToken){
		try{
			await store.dispatch('auth/getUserData'); //get current user data from api on page load

			mainRoute.children.push({ path: '/(home)?', name: 'home', component: () => import('pages/home/home.vue') });
		}
		catch(e){
			/*
			 * getting current user detail failed
			 * token must be invalid
			*/
			mainRoute.children.push({ path: '/(index)?', name: 'index', component: () => import('pages/index/index.vue') });
		}
	}
	else{
		/*
		 * user has not loggedIn
		 * show login page
		*/
		mainRoute.children.push({ path: '/(index|home)?', name: 'index', component: () => import('pages/index/index.vue') });
	}


	// Always leave this as last one
	if (process.env.MODE !== 'ssr') {
		mainRoute.children.push({path: '*', component: () => import('pages/errors/pagenotfound.vue')});
	}

	const Router = new VueRouter({
		scrollBehavior: () => ({ x: 0, y: 0 }),
		routes,
		// Leave these as they are and change in quasar.conf.js instead!
		// quasar.conf.js -> build -> vueRouterMode
		// quasar.conf.js -> build -> publicPath
		mode: process.env.VUE_ROUTER_MODE,
		base: process.env.VUE_ROUTER_BASE
	});
	return Router
}