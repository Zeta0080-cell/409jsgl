import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue';
import router from './router';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;

const app = createApp(App)

app.use(createPinia())
app.config.globalProperties.$axios = axios;  // 全局配置 axios
app.use(router); // 使用路由
app.use(store);
app.use(ElementPlus); // 使用 Element Plus UI 库
app.mount('#app');
