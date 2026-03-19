import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import translatePlugin from './translate-plugin'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    translatePlugin({
      mapPath: path.resolve(__dirname, 'en-map.json')
    })
  ],
  server: {
    port: 3001,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:5001',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
