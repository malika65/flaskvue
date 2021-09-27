
import { i18n } from 'boot/i18n.js';
import { StorageService } from './services/storage';
let locale = StorageService.getLocale();
if (locale) {
  i18n.locale = locale;
}

export const AppMenus = {
    
	UserTableHeaderItems: [
  {
    "label": i18n.t('id'),
    "align": "left",
    "sortable": false,
    "name": "id",
    "field": "id"
  },
  {
    "label": i18n.t('name'),
    "align": "left",
    "sortable": false,
    "name": "name",
    "field": "name"
  },
  {
    "label": i18n.t('email'),
    "align": "left",
    "sortable": false,
    "name": "email",
    "field": "email"
  },
  {
    "label": i18n.t('action'),
    "align": "right",
    "sortable": false,
    "name": "btnactions",
    "field": ""
  }
],
	BlacklistTableHeaderItems: [
  {
    "label": i18n.t('id'),
    "align": "left",
    "sortable": false,
    "name": "id",
    "field": "id"
  },
  {
    "label": i18n.t('name'),
    "align": "left",
    "sortable": false,
    "name": "name",
    "field": "name"
  },
  {
    "label": i18n.t('organization'),
    "align": "left",
    "sortable": false,
    "name": "organization",
    "field": "organization"
  },
  {
    "label": i18n.t('reiting'),
    "align": "left",
    "sortable": false,
    "name": "reiting",
    "field": "reiting"
  },
  {
    "label": i18n.t('action'),
    "align": "right",
    "sortable": false,
    "name": "btnactions",
    "field": ""
  }
],
	navbarSideLeftItems: [
  {
    "path": "/home",
    "label": i18n.t('home'),
    "icon": "home",
    "iconcolor": "primary",
    "target": "",
    "submenu": []
  },
  {
    "path": "/user",
    "label": i18n.t('user'),
    "icon": "perm_identity",
    "iconcolor": "primary",
    "target": "",
    "submenu": []
  },
  {
    "path": "/BlackList",
    "label": i18n.t('blacklist'),
    "icon": "list",
    "iconcolor": "primary",
    "target": "",
    "submenu": []
  }
],
	navbarTopLeftItems: [],
	navbarTopRightItems: [],

    exportFormats: {
        print: {
			label: 'Print',
			color: 'blue',
            icon: 'print',
            id: 'print',
            ext: '',
        },
        pdf: {
			label: 'Pdf',
			color: 'red',
            icon: 'picture_as_pdf',
            id: 'pdf',
            ext: 'pdf',
        },
        excel: {
			label: 'Excel',
			color: 'green',
            icon: 'grid_on',
            id: 'excel',
            ext: 'xlsx',
        },
        csv: {
			label: 'Csv',
			color: 'teal',
            icon: 'grid_on',
            id: 'csv',
            ext: 'csv',
        },
    },
    locales: {
  "fr": "French",
  "ru": "Russian",
  "zh_CN": "Chinese",
  "en": "English",
  "it": "Italian",
  "hi": "Hindi",
  "pt_PT": "Portuguese",
  "de": "German",
  "es": "Spanish",
  "ar": "Arabic"
}
}