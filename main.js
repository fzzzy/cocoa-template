import 'vite/modulepreload-polyfill';

import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'

createInertiaApp({
  resolve: name => {
    const pages = import.meta.glob('./Pages/**/*.vue', { eager: true });
    console.log(pages, name);
    const split = name.split('/');
    const stripped = split[split.length - 1];
    return pages[`./Pages/${stripped}.vue`]
  },
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .mount(el)
  },
})