import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/dist/",
  build: {
    outDir: "dist/",
    manifest: true,
    rollupOptions: {
      input: {
        main: './js/main.js',
      }
    }
  },
  plugins: [vue()],
})
