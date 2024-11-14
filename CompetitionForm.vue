<template>
  <el-form :model="form" label-width="100px">
    <el-form-item label="竞赛名称">
      <el-input v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="类别">
      <el-select v-model="form.category">
        <el-option label="校级一类" value="校级一类"></el-option>
        <el-option label="校级二类" value="校级二类"></el-option>
        <el-option label="校级三类" value="校级三类"></el-option>
        <el-option label="院级推荐" value="院级推荐"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="指导老师">
      <el-input v-model="form.instructor"></el-input>
    </el-form-item>
    <el-form-item label="获奖证书">
      <el-upload action="/api/upload" list-type="picture-card" :on-success="handleUploadSuccess">
        <i class="el-icon-plus"></i>
      </el-upload>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        name: '',
        category: '',
        instructor: '',
        certificate: '',
      },
    };
  },
  methods: {
    handleUploadSuccess(response) {
      this.form.certificate = response.url;  // 假设后端返回的图片URL
    },
    submitForm() {
      axios.post('/api/competitions', this.form).then(response => {
        this.$message.success('竞赛信息提交成功');
      });
    },
  },
};
</script>