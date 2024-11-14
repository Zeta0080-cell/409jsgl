<template>
    <el-form @submit.prevent="handleLogin" :model="loginForm" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="loginForm.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script>
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const store = useStore();
      const router = useRouter();
      const loginForm = ref({ username: '', password: '' });
  
      const handleLogin = () => {
        // 调用后端API登录
        axios.post('/api/login', loginForm.value).then(response => {
          store.dispatch('login', response.data.user);
          router.push('/');
        });
      };
  
      return { loginForm, handleLogin };
    },
  };
  </script>