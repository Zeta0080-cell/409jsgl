<template>
    <div>
      <el-page-header content="竞赛管理系统 - 管理员" />
      <el-divider />
      <el-row :gutter="20">
        <el-col :span="12">
          <h3>审核竞赛信息</h3>
          <ReviewCompetitionList />
        </el-col>
        <el-col :span="12">
          <h3>上传竞赛讲解视频</h3>
          <VideoUploadForm />
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  import ReviewCompetitionList from '../components/ReviewCompetitionList.vue';
  import VideoUploadForm from '../components/VideoUploadForm.vue';
  
  export default {
    components: {
      ReviewCompetitionList,
      VideoUploadForm,
    },
  };
  </script>
  
  <style scoped>
  h3 {
    margin-bottom: 16px;
  }
  </style>