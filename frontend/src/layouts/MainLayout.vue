<template>
    <q-layout view="hHh LpR lfr">
        <template v-if="$isLoggedIn">
            <q-header  bordered>
                <q-toolbar class="  ">
                    <q-btn flat @click="toggleLeftDrawer" round dense icon="menu"></q-btn>
                    <q-btn no-caps flat stretch to="/home" class="q-mr-lg">
                        <q-avatar size="36">
                            <img src="~assets/images/logo.png" alt="logo" class="my-5" />
                        </q-avatar>
                        <q-toolbar-title>
                        ProjectBL
                        </q-toolbar-title>
                    </q-btn>
                    <q-separator inset dark vertical></q-separator>
                    <template v-for="(menu, index) in navbarTopLeftItems">
                        <q-btn no-caps :icon="menu.icon" stretch flat :label="menu.label" :to="menu.path" v-if="!menu.submenu.length" :key="`topleftmenubtn-${index}`"></q-btn>
                        <q-btn-dropdown  no-caps :icon="menu.icon" stretch flat :label="menu.label" v-else  :key="`topleftmenudrop-${index}`" >
                            <q-list dense>
                                <q-item v-for="(submenu, subindex) in menu.submenu" :key="`topleftsubmenu-${subindex}`" clickable v-ripple :to="submenu.path">
                                    <q-item-section avatar v-if="submenu.icon">
                                        <q-avatar :icon="submenu.icon"></q-avatar>
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>{{ submenu.label }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                            </q-list>
                        </q-btn-dropdown>
                    </template>
                    <q-space></q-space>
                    <template v-for="(menu, index) in navbarTopRightItems">
                        <q-btn  no-caps :icon="menu.icon" stretch flat :label="menu.label" :to="menu.path" v-if="!menu.submenu.length" :key="`toprightmenu-${index}`"></q-btn>
                        <q-btn-dropdown no-caps :icon="menu.icon" stretch flat :label="menu.label" v-else  :key="`toprightmenudrop-${index}`" >
                            <q-list dense>
                                <q-item v-for="(submenu, subindex) in menu.submenu" :key="`toprightsubmenu-${subindex}`" clickable v-ripple :to="submenu.path">
                                    <q-item-section avatar v-if="submenu.icon">
                                        <q-avatar :icon="submenu.icon"></q-avatar>
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>{{ submenu.label }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                            </q-list>
                        </q-btn-dropdown>
                    </template>
                    <q-btn-dropdown no-caps stretch unelevated icon="account_circle">
                        <q-list dense style="min-width:200px">
                            <q-item  clickable v-ripple to="/account">
                                <q-item-section avatar>
                                    <q-avatar icon="account_box"></q-avatar>
                                </q-item-section>
                                <q-item-section>
                                    <q-item-label>{{ $t('my_account') }}</q-item-label>
                                </q-item-section>
                            </q-item>
                            <q-item  clickable v-ripple @click="startLogout()">
                                <q-item-section avatar>
                                    <q-avatar icon="exit_to_app"></q-avatar>
                                </q-item-section>
                                <q-item-section>
                                    <q-item-label>{{ $t('logout') }}</q-item-label>
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </q-btn-dropdown>
                </q-toolbar>
            </q-header>
            <q-drawer v-model="leftDrawer" show-if-above :width="250" :breakpoint="500" bordered   :mini="leftDrawerMini">
                <q-scroll-area class="fit   ">
                    <div class="text-center bg-primary q-pt-md">
                        <q-icon size="50px" color="white" name="account_box"></q-icon>
                        <div v-show="!leftDrawerMini" class="text-bold text-center text-capitalize q-pa-sm">
                            <span class="text-white">{{ $t('hi') }} {{ $UserName }}</span> 
                        </div>
                        <q-menu touch-position>
                            <q-list dense style="min-width:100px">
                                <q-item  clickable v-ripple to="/account">
                                    <q-item-section avatar>
                                        <q-avatar icon="account_box"></q-avatar>
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>{{ $t('my_account') }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                                <q-item  clickable v-ripple @click="startLogout()">
                                    <q-item-section avatar>
                                        <q-avatar icon="exit_to_app"></q-avatar>
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>{{ $t('logout') }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                            </q-list>
                        </q-menu>
                    </div>
                    <q-separator></q-separator>
                    <q-list>
                        <template v-for="(menu, index) in navbarSideLeftItems">
                            <q-item clickable q-ripple :to="menu.path" v-if="!menu.submenu.length" :key="`sideleftmenu-${index}`">
                                <q-item-section avatar v-if="menu.icon">
                                    <q-icon :color="menu.iconcolor || 'primary'" :name="menu.icon"></q-icon>
                                    <q-tooltip v-if="leftDrawerMini" transition-show="scale" transition-hide="scale" content-class="bg-accent" anchor="center right" self="center left" :offset="[10, 10]">
                                    {{ menu.label }}
                                    </q-tooltip>
                                </q-item-section>
                                <q-item-section>
                                    {{ menu.label }}
                                </q-item-section>
                            </q-item>
                            <q-expansion-item expand-separator :content-inset-level="0.5" group="leftmenu" :icon="menu.icon" :label="menu.label" v-else :key="`sideleftmenudrop-${index}`">
                                <q-list>    
                                    <q-item :to="submenu.path" clickable q-ripple v-for="(submenu, subindex) in menu.submenu" :key="`sideleftsubmenubtn-${subindex}`">
                                        <q-item-section avatar v-if="submenu.icon">
                                            <q-icon :color="submenu.iconcolor || 'primary'" :name="submenu.icon"></q-icon>
                                        </q-item-section>
                                        <q-item-section>
                                            {{ submenu.label }}
                                        </q-item-section>
                                    </q-item>
                                </q-list>
                            </q-expansion-item>
                        </template>
                    </q-list>
                </q-scroll-area>
            </q-drawer>
        </template>
        <template v-else>
            <q-header  bordered>
                <q-toolbar class="  ">
                    <q-btn no-caps flat stretch to="/home">
                        <q-avatar size="36">
                            <img src="~assets/images/logo.png" alt="logo" class="my-5" />
                        </q-avatar>
                        <q-toolbar-title>
                        ProjectBL
                        </q-toolbar-title>
                    </q-btn>
                </q-toolbar>
            </q-header>
        </template>
        <q-drawer :no-swipe-open="!componentFile" side="right" v-model="rightDrawer" :width="rightDrawerWidth" :breakpoint="500" overlay  elevated>
            <component v-if="rightDrawer" :is="componentFile" :api-path="pageUrl"></component>
            <q-btn style="position:absolute;top:10px;right:10px" unelevated dense round color="negative" icon="close" v-show="rightDrawer" @click="rightDrawer = !rightDrawer"></q-btn>
        </q-drawer>
        <q-footer  >
            <q-toolbar class="bg-grey-3 text-dark  justify-between">
                <div></div>
                <div>
                    {{ $t('language') }}:
                    <lang-switcher></lang-switcher>
                </div>
            </q-toolbar>
        </q-footer>
        <q-dialog v-model="pageDialog">
            <q-card style="width: 700px; max-width: 95vw;">
                <component v-if="pageDialog" :is="componentFile" :api-path="pageUrl" :model-bind="modelBind"></component>
            </q-card>
        </q-dialog>
        <q-dialog v-model="imageViewerDialog">
            <q-carousel
            transition-prev="scale"
            transition-next="scale"
            swipeable
            animated
            control-type="unelevated"
            control-color="primary"
            v-model="imageViewerCurrentSlide"
            :navigation="false"
            :arrows="imageViewerImages.length > 1"
            infinite
            :padding="false"
            height="auto"
            class="bg-dark rounded-borders"
            >
            <q-carousel-slide class="no-padding" v-for="(img, index) in imageViewerImages" :key="index" :name="index">
            <img style="max-width:100%;max-height:100%;" :src="img" />
            </q-carousel-slide>
            </q-carousel>
        </q-dialog>
        <q-page-container>
            <q-card v-if="pageErrors.length > 0" flat class="q-pa-sm">
                <div class="container-fluid">
                    <q-banner inline-actions>
                        <template v-slot:avatar>
                            <q-icon color="red" name="error"></q-icon>
                        </template>
                        <div class="text-weight-bold text-negative">{{ $t('unable_to_complete_request') }}</div>
                        <div class="q-py-sm" v-for="(msg, index) in pageErrors" :key="index">{{msg}}</div>
                        <template v-slot:action>
                            <q-btn flat icon="close" @click="pageErrors = []"></q-btn>
                        </template>
                    </q-banner>
                </div>
            </q-card>
            <keep-alive>
                <router-view></router-view>
            </keep-alive>
        </q-page-container>
    </q-layout>
</template>
<script>
	import { mapMutations, mapState, mapActions } from "vuex";
	export default {
		name: 'MainLayout',
		components: {
		},
		data: () => ({
		}),
		computed: {
			...mapState("pageComponents", ["pageComponent", "pageUrl", "modelBind", "imageViewerImages"]),
			leftDrawer: {
				get: function () {
					return this.$store.state.pageComponents.leftDrawer;
				},
				set: function (value) {
					this.$store.commit("pageComponents/setLeftDrawer", value);
				},
			},
			leftDrawerMini: {
				get: function () {
					return this.$store.state.pageComponents.leftDrawerMini;
				},
				set: function (value) {
					this.$store.commit("pageComponents/setLeftDrawerMini", value);
				},
			},
			pageDialog: {
				get: function () {
					return  this.$store.state.pageComponents.pageDialog
				},
				set: function (value) {
					this.$store.commit("pageComponents/setPageDialog", value);
				},
			},
			imageViewerCurrentSlide: {
				get: function () {
					return  this.$store.state.pageComponents.imageViewerCurrentSlide
				},
				set: function (value) {
					this.$store.commit("pageComponents/setImageViewerCurrentSlide", value);
				},
			},
			imageViewerDialog: {
				get: function () {
					return  this.$store.state.pageComponents.imageViewerDialog
				},
				set: function (value) {
					this.$store.commit("pageComponents/setImageViewerDialog", value);
				},
			},
			rightDrawer: {
				get: function () {
					return this.$store.state.pageComponents.rightDrawer;
				},
				set: function (value) {
					this.$store.commit("pageComponents/setRightDrawer", value);
				},
			},
			rightDrawerWidth: function(){
				if(this.$q.platform.is.desktop){
					return 400
				}
				return 320;
			},
			pageErrors: {
				get: function () {
					return this.$store.state.pageComponents.pageErrors;
				},
				set: function (value) {
					this.$store.commit("pageComponents/setPageErrors", value);
				},
			},
			componentFile() {
				if(this.pageComponent){
					return () => import(`pages/${this.pageComponent}.vue`);
				}
				return null;
			},
			navbarSideLeftItems(){
				return this.$menus.navbarSideLeftItems;
			},
			navbarTopLeftItems(){
				return this.$menus.navbarTopLeftItems;
			},
			navbarTopRightItems(){
				return this.$menus.navbarTopRightItems;
			},
		},
		created: function() {
			let showLeftDrawer = this.$q.platform.is.desktop;
			this.$store.commit("pageComponents/setLeftDrawer", showLeftDrawer);
			// Add a request interceptor
			this.$api.axios().interceptors.request.use(
				(config) => {
					this.$store.commit("pageComponents/setPageErrors", []);
					return config;
				},
				(error) => {
				// Do something with request error
				return Promise.reject(error);
			});

			this.$api.axios().interceptors.response.use(
				(response) => {
					return response
				},
				(error) => {
					if (error.request.status == 401) {
						if(this.$route.name != 'index'){
							this.logout();
							window.location = "/";
							return;
						}
					}
					else if (error.request.status == 403) {
						this.$router.push("/error/forbidden");
						return;
					}
					// reject error. Error will be handle by calling page.
					throw error
				}
			);
		},
		watch: {
			$route (to, from){
				this.$store.commit("pageComponents/setPageErrors", []);

				//close right drawer
				this.rightDrawer = false;
				this.$store.commit("pageComponents/setPageComponent", null);
			}
		},
		methods: {
			...mapActions('auth', ['logout']),
			toggleLeftDrawer() {
				if(this.leftDrawer && this.leftDrawerMini){
					this.leftDrawer = false;
				}
				else if(this.leftDrawer && !this.leftDrawerMini){
					this.leftDrawerMini = true;
				}
				else{
					this.leftDrawer = true;
					this.leftDrawerMini = false;
				}
			},

			startLogout (){
				this.logout();
				window.location = "/";//force reload of the page
			}
		},
	}
</script>

<style>
</style>
<style lang="scss">
	body.body--light {
		background: #EEEEEE
	}
</style>