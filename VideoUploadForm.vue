<template>
    <div class="video-upload-form">
      <el-form :model="videoForm" ref="videoForm" label-width="100px">
        <el-form-item label="竞赛ID" prop="competitionId">
          <el-input v-model="videoForm.competitionId" placeholder="请输入竞赛ID"></el-input>
        </el-form-item>
        <el-form-item label="视频文件" prop="videoFile">
          <el-upload
            action=""
            :file-list="fileList"
            :on-change="handleFileChange"
            :before-upload="() => false" 
            list-type="text"
          >
            <el-button type="primary">选择视频</el-button>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitVideo">上传视频</el-button>
        </el-form-item>
      </el-form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { ElMessage } from 'element-plus';
  
  export default {
    name: 'VideoUploadForm',
    setup() {
      const videoForm = ref({
        competitionId: '',
        videoFile: null,
      });
  
      const fileList = ref([]);
  
      const handleFileChange = (file) => {
        videoForm.value.videoFile = file.raw;
        fileList.value = [file];
      };
  
      const submitVideo = async () => {
        if (!videoForm.value.competitionId || !videoForm.value.videoFile) {
          ElMessage.warning('请填写所有信息并选择视频文件');
          return;
        }
  
        const formData = new FormData();
        formData.append('competitionId', videoForm.value.competitionId);
        formData.append('videoFile', videoForm.value.videoFile);
  
        try {
          const response = await fetch('/api/competitions/upload-video', {
            method: 'POST',
            body: formData,
          });
          
          if (response.ok) {
            ElMessage.success('视频上传成功');
            resetForm();
          } else {
            throw new Error();
          }
        } catch (error) {
          ElMessage.error('视频上传失败');
        }
      };
  
      const resetForm = () => {
        videoForm.value = { competitionId: '', videoFile: null };
        fileList.value = [];
      };
  
      return { videoForm, fileList, handleFileChange, submitVideo };
    },
  };
  </script>
  
  <style scoped>
  .video-upload-form {
    padding: 20px;
  }
  </style>