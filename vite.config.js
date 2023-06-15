import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/static/",
  build: {
    outDir: "static/",
    manifest: true,
    rollupOptions: {
      input: {
        main: './js/main.js',
      }
    },
  },
  server: {
    watch: {
      ignored: ['!**/*.py'],
    }
  },
  plugins: [vue()],
})
