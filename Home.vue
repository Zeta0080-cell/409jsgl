<template>
    <div>
      <el-page-header content="竞赛管理系统 - 普通成员" />
      <el-divider />
      <el-row :gutter="20">
        <el-col :span="12">
          <h3>提交竞赛信息</h3>
          <CompetitionForm />
        </el-col>
        <el-col :span="12">
          <h3>竞赛信息列表</h3>
          <CompetitionList />
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  import CompetitionForm from '../components/CompetitionForm.vue';
  import CompetitionList from '../components/CompetitionList.vue';
  
  export default {
    components: {
      CompetitionForm,
      CompetitionList,
    },
  };
  </script>
  
  <style scoped>
  h3 {
    margin-bottom: 16px;
  }
  </style>
