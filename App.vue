<template>
  <div id="app">
    <el-container>
      <el-header>
        <el-menu
          :default-active="activeMenu"
          mode="horizontal"
          @select="handleMenuSelect"
        >
          <el-menu-item index="/">主页</el-menu-item>
          <el-menu-item index="/admin">管理员页面</el-menu-item>
          <el-menu-item index="/login">登录</el-menu-item>
        </el-menu>
      </el-header>

      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>

  <div>
    <Home/>
    <Admin/>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from 'vuex';
import Home from './views/Home.vue'
import Admin from './views/Admin.vue'

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    // 设置活动菜单项
    const activeMenu = computed(() => route.path);

    // 菜单选择事件处理
    const handleMenuSelect = (path) => {
      if (path === '/admin' && !store.state.user?.isAdmin) {
        alert('仅管理员可访问该页面');
        return;
      }
      router.push(path);
    };

    return { activeMenu, handleMenuSelect };
  },

  components: {
    Home,
    Admin,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.el-header {
  background-color: #409eff;
  color: white;
}
.el-main {
  padding: 20px;
}
</style>
